from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField
from common.module_loading import import_by_path

class Fond(models.Model):

	display_name = models.CharField(unique = True, max_length = 20)
	total_shares = DecimalField()
	
	enterprise_object_id = models.PositiveIntegerField(editable = False)
	enterprise_type = models.ForeignKey(ContentType, related_name = '%(app_label)s')
	enterprise = generic.GenericForeignKey('enterprise_type', 'enterprise_object_id')
	
	@property
	def code_name(self):
		return '%.6d' % self.id	
		
	def get_share(self, user, create = False):	
		pass
	
	def modify_log(self, quantity):
		pass
	
	def get_price(self):
		pass
	
	def sell(self, user, quantity):
		pass
		
	def buy(self, user, quantity):
		pass
		
	class Meta:
		ordering = ['display_name']
		abstract = True	
		
class Share(models.Model):

	shares = DecimalField(editable = False)
	owner  = models.ForeignKey('accounts.Person', related_name = '%(app_label)s_shares')
	
	class Meta:
		abstract = True
		
class Log(models.Model):
	
	class Meta:
		abstract = True
		
def _get_fond(fond_type, attr):
	"""
		Example: get_fond_module('fund')
	"""
	return import_by_path('securities.%ss.models.%s' % (fond_type.lower(), attr))
	
def get_fond_class(fond_type):
	return _get_fond(fond_type, fond_type.capitalize())
	
from functools import partial

get_log_class = partial(_get_fond, attr = 'Log')
get_share_class = partial(_get_fond, attr = 'Share')