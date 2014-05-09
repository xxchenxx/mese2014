from rest_framework import serializers
from django.contrib.auth.models import User
import models

class AccountSerializer(serializers.Serializer):
	account_type = serializers.CharField(read_only = True)

class AdminSerializer(AccountSerializer):
	
	display_name = serializers.CharField(read_only = True)

class PersonSerializer(serializers.ModelSerializer, AccountSerializer):
	
	class Meta:
		model = models.Person
		
class EnterpriseSerializer(serializers.ModelSerializer, AccountSerializer):

	class Meta:
		model = models.Enterprise
		
class CompanySerializer(serializers.ModelSerializer, AccountSerializer):
	
	class Meta:
		model = models.Company
		
class BankSerializer(serializers.ModelSerializer, AccountSerializer):
	
	class Meta:
		model = models.Bank
		
class FundCompanySerializer(serializers.ModelSerializer, AccountSerializer):
	
	class Meta:
		model = models.FundCompany

class UserSerializer(serializers.ModelSerializer):

	is_admin = serializers.Field(source = 'is_staff')
	profile  = serializers.Field(source = 'profile')

	def transform_profile(self, obj, value):
		profile = obj.profile.info
		if profile is None:
			return {}
		cls_name = '%sSerializer' % profile.__class__.__name__
		a = globals()
		return globals()[cls_name](obj.profile.info).data
		
	class Meta:
		model = User
		fields = ('is_admin', 'username', 'profile', 'id')
		
def get_serializer_by_object(obj):
	return globals()['%sSerializer' % obj.__class__.__name__]