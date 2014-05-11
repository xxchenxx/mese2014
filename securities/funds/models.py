from django.db import models
from securities.models import Fond
import securities.models
from common.fields import DecimalField
from timeline.fields import FinancialYearField

class Fund(Fond):

	unit_net_worth = DecimalField()
	total_net_worth = DecimalField()
	
	class Meta:
		pass
		
class Share(securities.models.Share):
	
	fond = models.ForeignKey(Fund, related_name = 'shares')
	
class Log(models.Model):
	
	fund = models.ForeignKey(Fund, related_name = 'logs')
	increasement = DecimalField(editable = False)
	increased_rate = DecimalField(editable = False)
	year = FinancialYearField()
	
	class Meta:
		ordering = ['-year']
	