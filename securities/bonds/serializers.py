from rest_framework import serializers
from .models import Bond, Share
from accounts.serializers import AccountField

class BondSerializer(serializers.ModelSerializer):

	publisher = AccountField(required = False)

	class Meta:
		exclude = ('publisher_type', 'publisher_object_id','account', )
		model = Bond
		
class ShareSerializer(serializers.ModelSerializer):
	
	bond = BondSerializer(exclude = ['publisher'])
	
	class Meta:
		exclude = ('owner_type', 'owner_object_id', 'owner')
		model = Share
