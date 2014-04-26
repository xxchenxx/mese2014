#coding=utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from common.storage import SAEStorage
from file_upload.models import PrivateFile, PublicFile
from annoying.fields import AutoOneToOneField

class AccountBase(object):
	
	display_name = ''
	
class Admin(AccountBase):

	display_name = u'管理员'	
		
class Account(AccountBase, models.Model):
	
	display_name = models.CharField(max_length = 255)
	
	class Meta:
		abstract = True
		ordering = ['display_name']
		
class Person(Account):

	profile = models.OneToOneField('UserProfile', unique = True, related_name = 'person_info')
	cash = models.DecimalField(max_digits = 4, decimal_places = 2, default = 0)
	fixed_assets = models.DecimalField(max_digits = 4, decimal_places = 2, default = 0)
	debt_file = models.ForeignKey(PrivateFile, related_name = 'person_in_debt')
	consumption_reports = models.ManyToManyField(PrivateFile, related_name = 'person_owned_reports')
	
	class Meta:
		pass
	
class Company(Account):
	
	profile = models.OneToOneField('UserProfile', unique = True, related_name = 'company_info')
	description = models.TextField(null = True, blank = True)
	members = models.TextField(null = True, blank = True)
	phone_number = models.CharField(null = True, blank = True, max_length = 11)
	financial_reports = models.ManyToManyField(PrivateFile, related_name = 'company_owned_reports')
	
	class Meta:
		pass
		
class UserProfile(models.Model):
	
	COMPANY = 'CY'
	PERSON  = 'PN'
	ADMIN   = 'AN'
	
	USER_TYPE_CHOICES = (
			(COMPANY, 'company'),
			(PERSON,  'person'),
			(ADMIN,   'admin'),
	)
	
	user = AutoOneToOneField(User, unique = True, related_name = 'profile')
	user_type = models.CharField(max_length = 2, choices = USER_TYPE_CHOICES, default = PERSON)
	
	@property
	def info(self):
		if not hasattr(self, '_info'):
			try:
				if self.user_type == self.PERSON:
					self._info = self.person_info
				elif self.user_type == self.COMPANY:
					self._info = self.company_info
				else:
					self._info = Admin()
			except ObjectDoesNotExist:
				if self.user_type == self.PERSON:
					self._info = Person.objects.create(profile = self)
				elif self.user_type == self.COMPANY:
					self._info = Company.objects.create(profile = self)
		return self._info
	