from django.db import models
import securities.models import Fond
from common import fields

class Fund(Fond):

	unit_net_worth = fields.DecimalField()
	total_net_worth = fields.DecimialField()
	
	issued_by = models.ForiegnKey('accounts.FundCompany', related_name = 'issued_funds')
	
	class Meta(Fond.Meta):
		pass