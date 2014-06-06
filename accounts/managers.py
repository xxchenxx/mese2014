from django.db import models

class BankManager(models.Manager):

	def get_query_set(self):
		super(BankManager, self).get_query_set().filter(type = self.BANK)
		
class FundCompanyManager(models.Manager):
	
	def get_query_set(self):
		super(FundCompanyManager, self).get_query_set().filter(type = self.FUND_COMPANY)