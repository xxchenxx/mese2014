from django.db import models
from securities.models import Fond
from common import fields

class Fund(Fond):

	unit_net_worth = fields.DecimalField()
	total_net_worth = fields.DecimalField()
	
	issued_by = models.ForeignKey('accounts.FundCompany', related_name = 'issued_funds')
	
	class Meta(Fond.Meta):
		pass