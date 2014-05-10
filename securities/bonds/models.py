from django.db import models
from common.fields import DecimalField
from timeline.fields import FinancialYearField

import securities.models 

class Bond(securities.models.Fond):
	
	current_price = DecimalField()
	
class Share(securities.models.Share):
	
	fond = models.ForeignKey(Bond, related_name = 'shares')
	
class Log(models.Model):

	bond = models.ForeignKey(Bond, related_name = 'logs')

	beginning_price = DecimalField(editable = False)
	highest_price = DecimalField(editable = False)
	lowest_price = DecimalField(editable = False)
	final_price = DecimalField(editable = False)
	
	transcation_quantity = models.IntegerField(editable = False)
	transcation_money = DecimalField(editable = False)
	
	increasement = DecimalField(editable = False)
	increased_rate = DecimalField(editable = False)
	
	year = FinancialYearField()
	
	class Meta:
		ordering = ['-year']