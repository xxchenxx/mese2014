from django.db import models
from common.fields import DecimalField
from timeline.fields import FinancialYearField

import securities.models 

class Bond(securities.models.Fond):
	
	current_price = DecimalField()
	
	def get_price(self):
		return self.current_price
		
	def get_share_class(self):
		return Share
		
	def get_log_class(self):
		return Log
	
class Share(securities.models.Share):
	
	fond = models.ForeignKey(Bond, related_name = 'shares')
	
class Log(securities.models.Log):

	bond = models.ForeignKey(Bond, related_name = 'logs')

	beginning_price = DecimalField(editable = False)
	highest_price = DecimalField(editable = False)
	lowest_price = DecimalField(editable = False)
	final_price = DecimalField(editable = False)
	
	transcation_quantity = DecimalField(editable = False)
	transcation_money = DecimalField(editable = False)
	
	increasement = DecimalField(editable = False)
	increased_rate = DecimalField(editable = False)
	
	class Meta:
		ordering = ['-year']