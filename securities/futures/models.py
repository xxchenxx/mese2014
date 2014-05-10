from django.db import models

from securities.models import Fond
import securities.models
from common.fields import DecimalField
from timeline.fields import FinancialYearField

class Future(Fond):

	current_price = DecimalField()
	
class Share(securities.models.Share):
	
	fond = models.ForeignKey(Future, related_name = 'shares')
	
class Log(models.Model):

	future = models.ForeignKey(Future, related_name = 'logs')
	
	beginning_price = DecimalField(editable = False)
	last_final_price = DecimalField(editable = False)
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