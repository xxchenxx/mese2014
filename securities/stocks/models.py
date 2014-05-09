from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common import fields
from securities.models import Fond

class Stock(Fond):
	
	enterprise_object_id = models.PositiveIntegerField()
	enterprise_type = models.ForeignKey(ContentType)
	enterprise = generic.GenericForeignKey('enterprise_type', 'enterprise_object_id')
		
	class Meta(Fond.Meta):
		abstract = False
		
class StockShare(models.Model):
	
	owner = models.ForeignKey('accounts.Person', related_name = 'stock_shares')
	stock = models.ForeignKey(Stock)
	shares = models.IntegerField()
	
class StockLog(models.Model):

	stock = models.ForeignKey(Stock, related_name = 'logs')

	beginning_price = fields.DecimalField()
	last_final_price = fields.DecimalField()
	highest_price = fields.DecimalField()
	lowest_price = fields.DecimalField()
	final_price = fields.DecimalField()
	
	transcation_quantity = models.IntegerField()
	transcation_money = fields.DecimalField()
	
	loged_time = models.DateField()
	
	class Meta:
		ordering = ['loged_time']