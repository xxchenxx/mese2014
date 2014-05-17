from rest_framework import serializers
import logs.models
import models
import accounts.serializers

class HasFondSerializer(serializers.ModelSerializer):
	
	fond = serializers.SerializerMethodField('get_fond')
	
	def get_fond_serializer_class(self, obj):
		return get_fond_serializer_class(obj.fond.__class__.__name__.lower())
		
	def get_fond(self, obj):
		return self.get_fond_serializer_class(obj)(obj.fond).data

class FondSerializer(serializers.ModelSerializer):
	
	code_name = serializers.Field(source = 'code_name')
	enterprise = accounts.serializers.EnterpriseField()
	
	class Meta:
		exclude = ('enterprise_object_id', 'enterprise_type')
		
class ShareSerializer(HasFondSerializer):
	
	class Meta:
		fields = ('fond', 'shares')
		
class TradeLogSerializer(serializers.ModelSerializer):

	class Meta:
		model = logs.models.TradeLog
		exclude = ['owner', 'fond_type', 'fond_object_id', ]
		
def get_fond_serializer_class(fond_type):
	
	class ResultSerializer(FondSerializer):
		
		class Meta(FondSerializer.Meta):
			model = models.get_fond_class(fond_type)
			
	return ResultSerializer
	
def get_log_serializer_class(fond_type):
	
	class ResultSerializer(serializers.ModelSerializer):
		
		class Meta:
			model = models.get_log_class(fond_type)
			exclude = (fond_type.lower(),)
			
	return ResultSerializer
	
def get_share_serializer_class(fond_type):
	
	class ResultSerializer(ShareSerializer):
		
		class Meta(ShareSerializer.Meta):
			model = models.get_share_class(fond_type)
			
	return ResultSerializer