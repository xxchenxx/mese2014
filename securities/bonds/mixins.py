from common.mixins import *

__all__ = ['HasBondMixin']

class HasBondMixin(HasAssetsMixin):

	bond_shares = generic.GenericRelation(
			'bonds.Share',
			content_type_field = 'owner_type',
			object_id_field = 'owner_object_id'
	)
	
	def buy_bond(self, bond, money):
		if bond.published or self.assets < money:
			assert 1==2
			
		bond.apply_money(self, money)
		self.assets -= money
		
	
	class Meta:
		abstract = True