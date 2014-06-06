from rest_framework import serializers
from .models import Stock, Share, Application, Log
from accounts.serializers import AccountField

class StockSerializer(serializers.ModelSerializer):

	publisher = AccountField(required = False)

	class Meta:
		model = Stock
		exclude = ('publisher_type', 'publisher_object_id')
		
class LogSerializer(serializers.ModelSerializer):

	class Meta:
		model = Log
		exclude = ('stock',)
		
class ShareSerializer(serializers.ModelSerializer):
	
	stock = serializers.Field(source = 'stock.display_name')
	
	class Meta:
		model = Share
		exclude = ('owner_type', 'owner_object_id', 'owner')
		
class ApplicationSerializer(serializers.ModelSerializer):
	
	stock = StockSerializer()
	
	class Meta:
		model = Application
		exclude = ('applicant_type', 'applicant_object_id', 'applicant', 'command',)