from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField
import securities.models

from timeline.fields import FinancialYearField

class Stock(securities.models.Fond):

	current_price = DecimalField()
		
	def get_share_class(self):
		return share
		
	def get_price(self):
		return self.current_price
		
	def get_log_class(self):
		return Log
		
	class Meta:
		pass
		
class Share(securities.models.Share):
	
	fond = models.ForeignKey(Stock, related_name = 'shares')
	
class Log(securities.models.Log):

	stock = models.ForeignKey(Stock, related_name = 'logs')

	beginning_price = DecimalField(editable = False)
	last_final_price = DecimalField(editable = False)
	highest_price = DecimalField(editable = False)
	lowest_price = DecimalField(editable = False)
	final_price = DecimalField(editable = False)
	
	transcation_quantity = DecimalField(editable = False)
	transcation_money = DecimalField(editable = False)
	
	increasement = DecimalField(editable = False)
	increased_rate = DecimalField(editable = False)
	
	class Meta:
		ordering = ['-year']