from django.db import models
from django.contrib.auth.models import User

from common.fields import DecimalField

class Fond(models.Model):

	display_name = models.CharField(unique = True, max_length = 20)
	current_price = DecimalField()
	total_shares = models.IntegerField()
	
	@property
	def code_name(self):
		return '%.6d' % self.id
		
	class Meta:
		ordering = ['display_name']
		abstract = True		
		
	def get_share(self, user, create = False):	
		pass
	
	def modify_log(self, quantity):
		pass
	
	def sell(self, user, quantity):
		pass
		
	def buy(self, user, quantity):
		pass