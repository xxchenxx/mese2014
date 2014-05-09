from django.db import models
from securities.models import Fond
from common import fields

class Fund(Fond):

	unit_net_worth = fields.DecimalField()
	total_net_worth = fields.DecimalField()
	
	issued_by = models.ForeignKey('accounts.FundCompany', related_name = 'issued_funds')
	
	class Meta(Fond.Meta):
		pass
		
class FundShare(models.Model):
	
	user = models.ForeignKey('auth.User', related_name = 'fund_shares')
	fund = models.ForeignKey(Fund, related_name = 'shares')
	quantity = models.IntegerField(default = 0, blank = True, read_only = True)
	
class FundLog(models.Model):
	
	fund = models.ForeignKey(Fund, related_name = 'logs')