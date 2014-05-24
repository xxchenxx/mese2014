from __future__ import division
from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField

from exceptions import (AssetsNotEnough, SharesNotEnough)
from signals import application_updated

from decimal import Decimal

class Stock(models.Model):
	
	display_name = models.CharField(max_length = 255, default = '')
	
	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	
	current_price = DecimalField()
	created_time = models.DateTimeField(auto_now_add = True)
	
	def transfer(self, app_seller, app_buyer, shares):
		seller = app_seller.applicant
		buyer = app_buyer.applicant
		price = app_seller.price
		shares = Decimal(shares)
		app_seller.decrease_or_delete(shares)
		app_buyer.decrease_or_delete(shares)
		print """
			Seller: %s
			Buyer: %s
			Price: %f
			shares: %f""" %(seller, buyer, price, shares)
		money = Decimal(price) * shares
		seller.assets = F('assets') + money
		seller.save()
		buyer.assets = F('assets') - money
		buyer.save()
		
		share = Share.objects.get_share(seller, self, create = True)
		share.shares -= shares
		share.save()
		share = Share.objects.get_share(buyer, self, create = True)
		share.shares += shares
		share.save()
	
	def apply(self, applicant, price, command, shares):
		application = Application(stock = self, applicant = applicant, price = price, command = command, shares = shares)
		application.clean()
		application.save()
		application_updated.send(self, application = application)
		
		return application
		
	def update_price(self, price):
		if Decimal(price) - Decimal(self.current_price) > 1e-4:
			Log.objects.create(stock = self, price = price)
			self.current_price = price
			self.save()
	
	class Meta:
		ordering = ['-current_price', '-created_time']
	
class Log(models.Model):
	
	stock = models.ForeignKey(Stock, related_name = 'logs')
	price = DecimalField()
	created_time = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		ordering = ['-created_time']

class ApplicationManager(models.Manager):

	def fetch_suitable_applications(self, application):
		return self.filter(stock = application.stock, price = application.price).exclude(command = application.command)
		
class Application(models.Model):

	SELL = 'sell'
	BUY  = 'buy'
	COMMAND_CHOICE = (
		(SELL, 'sell'),
		(BUY,  'buy'),
	)

	applicant_type = models.ForeignKey(ContentType, null = True, blank = True)
	applicant_object_id = models.PositiveIntegerField(null = True, blank = True)
	applicant = generic.GenericForeignKey('applicant_type', 'applicant_object_id')
	
	stock = models.ForeignKey(Stock, related_name = 'applications')
	command = models.CharField(max_length = 4, choices = COMMAND_CHOICE)
	price  = DecimalField()
	shares = DecimalField()
	created_time = models.DateTimeField(auto_now_add = True)
	
	def decrease_or_delete(self, shares):
		self.shares -= shares
		if self.shares == Decimal(0) and self.id:
			self.delete()
		else:
			self.save()
	
	def get_share(self):
		if not hasattr(self, '_share'):
			self._share = Share.objects.get_share(owner = self.applicant, stock = self.stock)
			
		return self._share
	
	def clean(self):
		current_price, new_price = self.stock.current_price, Decimal(self.price)
		assert abs((current_price-new_price) / current_price) <= 0.2, "Stock price overflow."
		if self.command and self.command == self.BUY and self.applicant.assets < new_price * self.shares:
			raise AssetsNotEnough

		if self.command and self.command == self.SELL:
			self.get_share()
			if self._share is None or self._share.shares < self.shares:
				raise SharesNotEnough			
	
	def save(self, send = False, *args, **kwargs):
		if send and self.id is not None:
			application_updated.send(self, application = self)
		
		super(Application, self).save(*args, **kwargs)
	
	class Meta:
		ordering = ['created_time', 'price']
		
	objects = ApplicationManager()
		
class ShareManager(models.Manager):				
			
	def get_share(self, owner, stock, create = False, **kwargs):
		try:
			return owner.stock_shares.get(stock = stock)
		except Share.DoesNotExist:
			if create:
				return Share(owner = owner, stock = stock, **kwargs)
		
class Share(models.Model):
	
	owner_type = models.ForeignKey(ContentType, null = True, blank = True, related_name = 'stock_shares')
	owner_object_id = models.PositiveIntegerField(null = True, blank = True)
	owner = generic.GenericForeignKey('owner_type', 'owner_object_id')
	
	stock = models.ForeignKey(Stock, related_name = 'shares')
	shares = DecimalField()
	
	objects = ShareManager()
	
def process_application_updated(sender, **kwargs):
	application = kwargs.get('application', None)
	assert isinstance(application, Application), "There must be an application argument."
	stock = application.stock
	
	application_sets = []
	quantity = application.shares
	for _application in Application.objects.fetch_suitable_applications(application).prefetch_related():
		application_sets.append((_application, min(_application.shares, quantity)))
		quantity -= _application.shares
		if quantity <= 0:
			break
	if not application_sets:
		return
	print application_sets
		
	for _application, share in application_sets:
		if application.command == Application.BUY:
			seller, buyer = _application, application
		else:
			seller, buyer = application, _application
		stock.transfer(seller, buyer, share)	
		
	if quantity < 0:
		application_sets.pop()	

	Application.objects.filter(id__in = (app[0].id for app in application_sets)).delete()
	stock.update_price(application.price)
	
application_updated.connect(process_application_updated)