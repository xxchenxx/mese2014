from rest_framework import serializers
from .models import Fund, Share
from accounts.serializers import AccountField

class FundSerializer(serializers.ModelSerializer):

	publisher = AccountField(required = False)

	class Meta:
		exclude = ('publisher_type', 'publisher_object_id','account', )
		model = Fund
		
class ShareSerializer(serializers.ModelSerializer):
	
	fund = FundSerializer(exclude = ['publisher'])
	
	class Meta:
		exclude = ('owner_type', 'owner_object_id', 'owner')
		model = Share