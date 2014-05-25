from common.mixins import *

__all__ = ['OwnFundMixin']

class OwnFundMixin(models.Model):
	
	funds = generic.GenericRelation(
			'funds.Fund',
			content_type_field = 'owner_type',
			object_id_field = 'owner_object_id'
	)	
	
	class Meta:
		abstract = True