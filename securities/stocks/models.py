from django.db import models
from common import fields
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Stock(models.Model):
	
	enterprise_object_id = models.PositiveIntegerField()
	enterprise_type = models.ForeignKey()
	enterprise = generic.GenericForeignKey('enterprise_type', 'enterprise_object_id')
	
	market_cap = fields.DecimalField()
	total_shares = models.IntegerField()
	
	@property
	def code_name(self):
		return '%.6d' % self.id
		
class StockShare(models.Model):
	
	owner = models.ForeignKey('accounts.Person')
	stock = models.ForeignKey(Stock)
	shares = models.IntegerField()