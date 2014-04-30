from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common import fields
from securities.models import Fond

class Stock(Fond):
	
	enterprise_object_id = models.PositiveIntegerField()
	enterprise_type = models.ForeignKey(ContentType)
	enterprise = generic.GenericForeignKey('enterprise_type', 'enterprise_object_id')
	
	market_cap = fields.DecimalField()
	total_shares = models.IntegerField()
	
	@property
	def code_name(self):
		return '%.6d' % self.id
		
	class Meta(Fond.Meta):
		abstract = False
		
class StockShare(models.Model):
	
	owner = models.ForeignKey('accounts.Person', related_name = 'stock_shares')
	stock = models.ForeignKey(Stock)
	shares = models.IntegerField()
	
class StockLog(models.Model):

	stock = models.ForeignKey(Stock, related_name = 'logs')

	highest_price = fields.DecimalField()
	lowest_price = fields.DecimalField()
	final_price = fields.DecimalField()
	
	transcation_volume = models.IntegerField()
	transcation_turnover = models.IntegerField()
	
	loged_time = models.DateField()
	
	class Meta:
		ordering = ['loged_time']