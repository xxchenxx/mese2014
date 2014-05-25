from common.mixins import *
from models import Share
from exceptions import BondPublished

__all__ = ['HasBondMixin', 'OwnBondMixin']

class HasBondMixin(HasAssetsMixin):

	bond_shares = generic.GenericRelation(
			'bonds.Share',
			content_type_field = 'owner_type',
			object_id_field = 'owner_object_id'
	)
	
	def buy_bond(self, bond, money):
		bond.check_published()
		self.check_assets(money)
		bond.apply_money(self, money)
		self.dec_assets(money)
		
	def get_share(self, bond, create = False, **kwargs):
		try:
			return self.bond_shares.get(bond = bond)
		except Share.DoesNotExist:
			if create:
				return Share(owner = self, stock = stock, **kwargs)

	class Meta:
		abstract = True
		
class OwnBondMixin(models.Model):
	
	bonds = generic.GenericRelation(
			'bonds.Bond',
			content_type_field = 'publisher_type',
			object_id_field = 'publisher_object_id'
	)
	
	class Meta:
		abstract = True