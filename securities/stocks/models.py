from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField

from exceptions import (AssetsNotEnough, SharesNotEnough)
from signals import application_updated

class Stock(models.Model):
	
	display_name = models.CharField(max_length = 255, default = '')
	
	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	
	current_price = DecimalField()
	created_time = models.DateTimeField(auto_now_add = True)
	
	def apply(applicant, price, command, shares):
		assert command in (Application.BUY, Application.SELL), 'Application command must be either sell or buy.'
		
		if command == Application.BUY:
			if applicant.assets < price * shares:
				raise AssetsNotEnough
		else:
			try:
				share = applicant.stock_shares.all().get(stock = self)
			except Share.DoesNotExist:
				raise SharesNotEnough	
			if share.shares < shares:
				raise SharesNotEnough
		
		application = Application.objects.create(applicant = applicant, price = price, command = command, shares = shares)
		application_updated.send(self, application = application)
		
		return application
	
	class Meta:
		ordering = ['-current_price', '-created_time']
	
class Log(models.Model):
	
	stock = models.ForeignKey(Stock, related_name = 'logs')
	price = DecimalField()
	created_time = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		ordering = ['-created_time']

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
	
	def save(self, *args, **args):
		if self.id is not None:
			application_updated.send(self, application = self)
		
		super(Application, self).save(*args, **kwargs)
	
	class Meta:
		ordering = ['created_time', 'price']
		
class Share(models.Model):
	
	owner_type = models.ForeignKey(ContentType, null = True, blank = True, related_name = 'stock_shares')
	owner_object_id = models.PositiveIntegerField(null = True, blank = True)
	owner = generic.GenericForeignKey('owner_type', 'owner_object_id')
	
	stock = models.ForeignKey(Stock, related_name = 'shares')
	shares = DecimalField()
	
def process_application_updated(sender, **kwargs):
	application = kwargs.get('application', None)
	assert isinstance(application, Application)
	# Wait for implementing.
	
application_updated.connect(process_application_updated)