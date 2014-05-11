from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
import models
from file_upload.serializers import PrivateFileSerializer

class AccountSerializer(serializers.Serializer):

	account_type = serializers.CharField(read_only = True)
	url = serializers.SerializerMethodField('get_url')
	
	def get_url(self, obj):
		return reverse('user-profile', kwargs = {'pk':obj.profile.user.pk})

class AdminSerializer(AccountSerializer):
	
	display_name = serializers.CharField(read_only = True, required = False)
		
class EnterpriseSerializer(serializers.ModelSerializer, AccountSerializer):

	class Meta:
		model = models.Enterprise
		
class HyperlinkedCompanySerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = models.Company
		fields = ('url', 'display_name')
		lookup_field = 'pk'
		

class PersonSerializer(serializers.ModelSerializer, AccountSerializer):
	
	company = serializers.Field(source = 'company.display_name')#HyperlinkedCompanySerializer()
	debt_file = PrivateFileSerializer()
	
	class Meta:
		model = models.Person	
		exclude = ['consumption_reports', 'company_type', 'company_object_id']
		
class CompanySerializer(serializers.ModelSerializer, AccountSerializer):
	
	members = PersonSerializer(many = True, required = False)

	class Meta:
		model = models.Company
		exclude = ['financial_reports']
		
class BankSerializer(serializers.ModelSerializer, AccountSerializer):
	
	class Meta:
		model = models.Bank
		
class FundCompanySerializer(serializers.ModelSerializer, AccountSerializer):
	
	class Meta:
		model = models.FundCompany

class UserSerializer(serializers.ModelSerializer):

	is_admin = serializers.Field(source = 'is_staff')
	profile  = serializers.SerializerMethodField('get_profile')

	def get_profile(self, obj):
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