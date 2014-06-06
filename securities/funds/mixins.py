from common.mixins import *
from models import Share

__all__ = ['OwnFundMixin', 'HasFundMixin']

class HasFundMixin(models.Model):
	
	fund_shares = generic.GenericRelation(
			'funds.Share',
			content_type_field = 'owner_type',
			object_id_field = 'owner_object_id',
	)

	def get_fund_share(self, fund, create = False, **kwargs):
		try:
			return self.fund_shares.get(fund = fund)
		except Share.DoesNotExist:
			if create:
				return Share(owner = self, fund = fund, **kwargs)
	
	def buy_fund(self, fund, money):
		assert fund.can_buy()
		print money
		self.check_assets(money)
		fund.apply_money(self, money)
		self.dec_assets(money)
		
	class Meta:
		abstract = True

class OwnFundMixin(models.Model):
	
	funds = generic.GenericRelation(
			'funds.Fund',
			content_type_field = 'owner_type',
			object_id_field = 'owner_object_id'
	)	
	
	class Meta:
		abstract = True