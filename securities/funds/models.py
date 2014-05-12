from django.db import models
from securities.models import Fond
import securities.models
from common.fields import DecimalField
from timeline.fields import FinancialYearField

class Fund(Fond):

	unit_net_worth = DecimalField()
	total_net_worth = DecimalField()
	
	def get_price(self):
		return self.unit_net_worth
		
	def get_share_class(self):
		return Share
		
	def get_log_class(self):
		return log
	
	class Meta:
		pass
		
class Share(securities.models.Share):
	
	fond = models.ForeignKey(Fund, related_name = 'shares')
	
class Log(securities.models.Log):
	
	fund = models.ForeignKey(Fund, related_name = 'logs')
	increasement = DecimalField(editable = False)
	increased_rate = DecimalField(editable = False)
	
	class Meta:
		ordering = ['-year']
	