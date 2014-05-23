#coding=utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from common.storage import SAEStorage

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField
from files.models import PrivateFile, PublicFile, File
from annoying.fields import AutoOneToOneField
	
import managers

# Abstract logical interfaces.

class HasAssetsModel(models.Model):
	
	assets = DecimalField()
	
	class Meta:
		abstract = True

class HasReportsModel(object):
	
	@classmethod
	def has_field(cls, field_name):
		try:
			return cls._meta.get_field_by_name(field_name)
		except:
			pass
	
	def upload_reports(self, file_ids, **kwargs):
		field_name = kwargs.pop('field_name',self.report_field)
		field = self.has_field(field_name)
		if not field:
			return
		
		objects = PrivateFile.objects.only('pk')
		if isinstance(file_ids, (list, tuple)):
			files = objects.filter(pk__in = file_ids) if isinstance(file_ids, (str,int)) else files
		elif isinstance(file_ids, (int, str)):
			files = objects.filter(pk = int(file_ids))
		else:
			files	=	(file_ids,)

		if isinstance(field, models.ForeignKey):
			setattr(self, field_name, files[0])
			self.save()
		else:
			getattr(self, field_name).add(*files)		

class HasFundModel(models.Model):
	
	funds = generic.GenericRelation(
			'funds.Fund',
			content_type_field = 'owner_type',
			object_id_field = 'owner_object_id'
	)	
	
	class Meta:
		abstract = True	
	
class UserProfile(models.Model):
	
	user = AutoOneToOneField(User, unique = True, related_name = 'profile')
	
	info_type = models.ForeignKey(ContentType, null = True, blank = True)
	info_object_id = models.PositiveIntegerField(null = True, blank = True)
	info_object = generic.GenericForeignKey('info_type', 'info_object_id')
	
	@property
	def info(self):
		if self.user.is_staff:
			if not hasattr(self, '_info'):
				self._info = Admin(self)
				
			return self._info
		else:
			return self.info_object
			
	@info.setter
	def info(self, obj):
		if self.user.is_staff:
			return
		self.info_object = obj	

# Models definition.		
		
class Account(models.Model):
	
	display_name = models.CharField(max_length = 50, default = '')
	profile_object = generic.GenericRelation(
			'UserProfile',
			content_type_field = 'info_type',
			object_id_field = 'info_object_id'
	)
	
	class Meta:
		abstract = True
	
class PersonalModel(Account, HasAssetsModel):

	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICE = (
			(MALE, 'male'),
			(FEMALE, 'female'),
	)
	
	gender = models.CharField(max_length = 1, default = MALE)
	position = models.CharField(max_length = 20, default = '')
	
	class Meta:
		abstract = True
	
class Media(Account):
	
	contact = models.CharField(max_length = 20, default = '')	
		
class Section(models.Model):

	display_name = models.CharField(max_length = 20, default = '')
	
class Industry(models.Model):

	section = models.ForeignKey(Section, related_name = 'industries')
	display_name = models.CharField(max_length = 20, default = '')		
		
class Person(PersonalModel, HasReportsModel):

	company = models.ForeignKey('Company', related_name = 'members')
	industry = models.ForeignKey(Industry, related_name = 'persons')
	debt_files = models.ManyToManyField(PrivateFile, related_name = 'debt_files_owners')
	consumption_reports = models.ManyToManyField(PrivateFile, related_name = 'consumption_reports_owners')
	
	report_field = 'consumption_reports'
	
class Government(PersonalModel):

	pass
	
class Enterprise(Account, HasAssetsModel, HasReportsModel):

	description = models.CharField(max_length = 255, default = '')
	contact = models.CharField(max_length = 20, default = '')
	financial_reports = models.ManyToManyField(PrivateFile, related_name = '%(class)ss')
	
	report_field = 'financial_reports'
	
	class Meta:
		abstract = True
		
class Company(Enterprise):

	industry = models.ForeignKey(Industry, related_name = 'companies', null = True)
	
class FundCompany(Enterprise, HasFundModel):

	pass
	
class Bank(Enterprise, HasFundModel):
	
	pass	
	
class Fund(Account, HasAssetsModel):

	pass