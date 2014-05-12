from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField
from common.module_loading import import_by_path

from timeline.fields import FinancialYearField

from logs.models import TradeLog

from decimal import Decimal

import exceptions

class Fond(models.Model):

	display_name = models.CharField(unique = True, max_length = 20)
	total_shares = DecimalField()
	
	enterprise_object_id = models.PositiveIntegerField(editable = False)
	enterprise_type = models.ForeignKey(ContentType, related_name = '%(app_label)s')
	enterprise = generic.GenericForeignKey('enterprise_type', 'enterprise_object_id')
	
	@property
	def code_name(self):
		return '%.6d' % self.id	
	
	def get_log_class(self):
		return Log
	
	def modify_log(self, quantity, money):
		#Can be override
		log = self.get_log_class.objects.get_current_log()
		log.transcation_quantity += quantity
		log.transcation_money += money
		log.save()		
	
	def get_price(self):
		#Must be implemented
		pass
		
	def calc_total_price(self, shares):
		return self.get_price()*shares
		
	def get_share_class(self):
		#Must be implemented
		return Share
		
	def get_personal_share(self, person, create = False):
		share_class = self.get_share_class()
		try:
			share = share_class.objects.get(owner = person)
		except:
			if create:
				share = share_class(owner = person, fond = self)
			else:
				return
		
		return share
	
	def post_buy(self, person, quantity, money, share):
		pass
	
	def buy(self, person, quantity):
		total_price = self.calc_total_price()
		if total_price > person.assets:
			raise exceptions.MoneyNotEnough
			
		person.assets -= total_price
		share = get_personal_share(person, True)
		share.shares += Decimal(quantity)
		TradeLog.objects.create(
				owner = person,
				action = 'buy',
				fond = self,
				quantity = quantity,
				money = total_price,
		)
		self.modify_log(quantity, total_price)
		self.post_buy(person, quantity, total_price, share)
		
		person.save()
		share.save()
		
	def post_sell(self, person, quantity, money, share):
		pass
		
	def sell(self, person, quantity):
		share = self.get_personal_share(person)
		if share is None or share.shares < quantity:
			raise exceptions.SharesNotEnough
			
		total_price = self.calc_total_price(quantity)
		person.assets += total_price
		share.shares -= Decimal(quantity)
		TradeLog.objects.create(
				owner = person,
				action = 'sell',
				fond = self,
				quantity = quantity,
				money = total_price,		
		)
		self.modify_log(quantity, money)
		self.post_sell(person, quantity, money, share)
		
		person.save()
		if share.shares == 0:
			share.delete()
		else:
			share.save()
		
	class Meta:
		ordering = ['display_name']
		abstract = True	
		
class Share(models.Model):

	shares = DecimalField(editable = False)
	owner  = models.ForeignKey('accounts.Person', related_name = '%(app_label)s_shares')
	
	class Meta:
		abstract = True
		
class LogManager(models.Manager):
		
	def get_current_log(self):
		return self.order_by('-year')[0]
		
class Log(models.Model):
	
	year = FinancialYearField()
	objects = LogManager()
	
	class Meta:
		abstract = True
		
def _get_fond(fond_type, attr):
	"""
		Example: get_fond_module('fund')
	"""
	return import_by_path('securities.%ss.models.%s' % (fond_type.lower(), attr))
	
def get_fond_class(fond_type):
	return _get_fond(fond_type, fond_type.capitalize())
	
from functools import partial

get_log_class = partial(_get_fond, attr = 'Log')
get_share_class = partial(_get_fond, attr = 'Share')