from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField, TimeDeltaField
from common.mixins import get_inc_dec_mixin

from django.db import connection

from decimal import Decimal

class Fund(models.Model):

	OPEN = 'open'
	CLOSE = 'close'
	TYPE_CHOICE = (
		(OPEN, 'open'),
		(CLOSE, 'close'),
	)
	
	display_name = models.CharField(max_length = 255, default = '')

	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	
	account = models.OneToOneField('accounts.Fund', related_name = 'fund', null = True, blank = True)
	
	published = models.BooleanField(default = False)
	
	min_return_rate = DecimalField()
	max_return_rate = DecimalField()
	inital_money = DecimalField()
	lasted_time = TimeDeltaField()
	published_time = DecimalField()
	
	fund_type = models.CharField(max_length = 10, choices = TYPE_CHOICE)
	
	created_time = models.DateTimeField(auto_now_add = True)
	
	def __init__(self, *args, **kwargs):
		self.__total_money = None
		return super(Fund, self).__init__(*args, **kwargs)
	
	def apply_money(self, actor, money):
		pass
	
	def can_buy(self):
		return True
	
	def get_total_money(self):
		if self.__total_money is None:
			self.__total_money = Share.objects.get_total_money(self)
			
		return self.__total_money
	
	class Meta:
		ordering = ['-created_time']
	
class ClosedEndFund(Fund):
	
	def can_buy(self):
		return not self.published
	
	class Meta:
		proxy = True
	
class OpenEndFund(Fund):

	class Meta:
		proxy = True
		
class ShareManager(models.Manager):
	
	def get_total_money(self, fund):
		cursor = connection.cursor()
		cursor.execute("SELECT SUM(assets) FROM %s GROUP BY id HAVING id=%d" % Share._meta.db_table, [fund.id])
		return cursor.fetchone()[0]
		
class Share(get_inc_dec_mixin(['money'])):

	owner_type = models.ForeignKey(ContentType, null = True, blank = True, related_name = 'fund_shares')
	owner_object_id = models.PositiveIntegerField(null = True, blank = True)
	owner = generic.GenericForeignKey('owner_type', 'owner_object_id')
	
	fund = models.ForeignKey(Fund, related_name = 'shares')
	money = DecimalField()
	percentage = DecimalField()
	
	def pre_set_money(self, value):
		total_money = self.fund.get_total_money()
		new_total_money = total_money + value
		cursor = connection.cursor()
		if not self.fund.published:
			cursor.execute(
					"""UPDATE funds_share SET percentage=CASE id WHEN %(id)d THEN (percentage/100*%(total)d+%(value)s)/%(new_total)d*100 
						ELSE percentage*%(total)d/%(new_total)d END WHERE fund_id=%(fund_id)d
					""" %
					{
						'total': total_money,
						'new_total': new_total_money,
						'id': self.id,
						'fund_id': self.fund.id,
						'value': value,
					}
			)
		else:
			cursor.execute(
					"""UPDATE funds_share SET percentage"""
			
	
	objects = ShareManager()
	
	class Meta:
		ordering = ['-money']