#encoding=utf8
from common.mixins import *
from models import Share
from notifications import send_notification
from django.core.exceptions import ValidationError

__all__ = ['OwnFundMixin', 'HasFundMixin']

class HasFundMixin(models.Model):
	
	fund_shares = generic.GenericRelation(
			'funds.Share',
			content_type_field = 'owner_type',
			object_id_field = 'owner_object_id',
	)

	def ransom(self, fund, money):
		try:
			share = self.shares.get(fund = fund)
		except Share.DoesNotExist:
			raise ValidationError("You have no shares of this fund!")
		if share.money < money:
			raise ValidationError("There is not enough money in your fund!")
			
		send_notification(recipient = fund.account)

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
