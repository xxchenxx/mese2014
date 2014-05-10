from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField

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