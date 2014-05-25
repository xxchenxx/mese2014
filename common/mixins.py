from django.db import models
from common.fields import DecimalField

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from functools import partial
from exceptions import AssetsNotEnough

def get_inc_dec_mixin(fields = []):

	class IncDecMixin(models.Model):
		
		def __set_item(self, field_name, value, commit = True, reload = False):
			if self.id is None:
				setattr(self, field_name, value)
				if commit:
					self.save()
				return
			
			setattr(self, field_name, getattr(self, field_name)+value)
			if commit:
				self.save()
			if reload:
				self = self.__class__.objects.get(pk = self.id)			
		
		def __inc(self, field_name, value, commit = True, reload = False):
			return self.__set_item(field_name, value, commit, reload)
			
		def __dec(self, field_name, value, commit = True, reload = False):
			return self.__set_item(field_name, -value, commit, reload)
		
		def __getattr__(self, name):
			action, field_name = name[:3], name[4:]
			if field_name not in fields or action not in ('inc', 'dec'):
				raise AttributeError, name
				
			if action == 'inc':
				return partial(self.__inc, field_name)
			else:
				return partial(self.__dec, field_name)
		
		class Meta:
			abstract = True
		
	return IncDecMixin

class HasAssetsMixin(get_inc_dec_mixin(['assets'])):
	
	assets = DecimalField()
	
	def check_assets(self, assets):
		if self.assets < assets:
			raise AssetsNotEnough
		
		return True
	
	class Meta:
		abstract = True