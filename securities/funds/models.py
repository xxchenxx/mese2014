from django.db import models
from securities.models import Fond
import securities.models
from common.fields import DecimalField
from timeline.fields import FinancialYearField

class Fund(Fond):

	unit_net_worth = DecimalField()
	total_net_worth = DecimalField()
	
	current_price_field = 'unit_net_worth'
	
	def get_price(self):
		return self.unit_net_worth
		
	def get_share_class(self):
		return Share
		
	def get_log_class(self):
		return log
	
	def modify_log(self):
		return
	
	class Meta:
		pass
		
class Share(securities.models.Share):
	
	fond = models.ForeignKey(Fund, related_name = 'shares')
	
class Log(securities.models.Log):
	
	fond = models.ForeignKey(Fund, related_name = 'logs')
	last_final_price = DecimalField(editable = False)
	increasement = DecimalField(editable = False)
	increased_rate = DecimalField(editable = False)
	
	class Meta:
		ordering = ['-year']
	