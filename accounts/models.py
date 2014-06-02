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

from django.db import connection

import managers

from common.mixins import HasAssetsMixin
from securities.mixins import *
from transfer.mixins import *

# Abstract logical interfaces.

class HasReportsMixin(object):
	
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
			files = (file_ids,)

		if isinstance(field, models.ForeignKey):
			setattr(self, field_name, files[0])
			self.save()
		else:
			getattr(self, field_name).add(*files)
		
# Models definition.
	
class UserProfile(models.Model):
	
	user = AutoOneToOneField(User, unique = True, related_name = 'profile')
	
	info_type = models.ForeignKey(ContentType, null = True, blank = True)
	info_object_id = models.PositiveIntegerField(null = True, blank = True)
	info_object = generic.GenericForeignKey('info_type', 'info_object_id')
	
	def create_info(self, class_name, save = True, **kwargs):
		if self.info_object is None:
			self.info_object = globals()[class_name].objects.create(**kwargs)
			if save:
				self.save()
		return self.info_object
	
		@property
		def info(self):
			return self.info_object
		@info.setter
		def info(self, obj):
			if self.user.is_staff:
				return
			self.info_object = obj					
class Account(models.Model):
	
	display_name = models.CharField(max_length = 50, default = '')
	profile_object = generic.GenericRelation(
			'UserProfile',
			content_type_field = 'info_type',
			object_id_field = 'info_object_id'
	)
	
	@property
	def profile(self):
		return self.profile_object.all()[0]
	
	class Meta:
		abstract = True
	
class PersonalModel(Account, HasAssetsMixin, HasFundMixin, CanTransferMixin):

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
		
class Person(PersonalModel, HasReportsMixin, HasStockBondMixin, CanStoreMixin):

	company = models.ForeignKey('Company', related_name = 'members')
	industry = models.ForeignKey(Industry, related_name = 'persons')
	debt_files = models.ManyToManyField(PrivateFile, related_name = 'debt_files_owners')
	consumption_reports = models.ManyToManyField(PrivateFile, related_name = 'consumption_reports_owners')
	
	report_field = 'consumption_reports'
	
	def save(self, *args, **kwargs):
		if self.id is None:
			self.industry = self.company.industry
		super(Person, self).save(*args, **kwargs)
	
class Government(PersonalModel, HasStockBondMixin):

	pass
	
class Enterprise(Account, HasAssetsMixin, HasReportsMixin, HasStockBondMixin, HasFundMixin, CanStoreMixin, CanTransferMixin):

	description = models.CharField(max_length = 255, default = '')
	contact = models.CharField(max_length = 20, default = '')
	financial_reports = models.ManyToManyField(PrivateFile, related_name = '%(class)ss')
	
	report_field = 'financial_reports'
	
	class Meta:
		abstract = True
		
class Company(Enterprise):

	industry = models.ForeignKey(Industry, related_name = 'companies', null = True)
	
class FundCompany(Enterprise, OwnFundMixin):

	pass
	
class Bank(Enterprise, OwnFundMixin):
	
	rate = DecimalField()
	
	def share_profits(self):
		rate = rate /100
		cursor = connection.cursor()
		cursor.execute(
				"""UPDATE transfer_deposits SET money = ROUND(money*(1+%s), 4) WHERE bank_id=%d""" % self.id
		)
	
class Fund(Account, HasAssetsMixin):

	pass