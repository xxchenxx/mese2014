from django.db import models
from django.db.models import F

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField
from common.mixins import get_inc_dec_mixin
from exceptions import BondPublished

class Bond(models.Model):
	
	GOVERNMENT = 'GOV'
	ENTERPRISE = 'ENT'
	TYPE_CHOICE = (
			(GOVERNMENT, 'Government'),
			(ENTERPRISE, 'Enterprise'),
	)
	
	display_name = models.CharField(max_length = 255, default = '')
	
	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	type = models.CharField(max_length = 3, choices = TYPE_CHOICE)
	
	published = models.BooleanField(default = False)
	
	interest_rate = DecimalField()
	lasted_time = models.TimeField()
	published_time = models.DateTimeField()
	created_time = models.DateTimeField(auto_now_add = True)
	
	def check_published(self):
		if self.published:
			raise BondPublished
	
	def clean_fields(self, *args, **kwargs):
		if self.type is None:
			self.type = self.GOVERNMENT if self.publisher.__class__.__name__ == 'Government' else self.ENTERPRISE
			
		super(Bond, self).clean_fields(*args, **kwargs)
	
	def apply_money(self, actor, money):
		share = actor.get_share(self, create = True, money = money).inc_money(money)
		self.publisher.inc_assets(money)
	
	class Meta:
		ordering = ['-created_time']
	
class ShareManager(models.Manager):
	pass
	
class Share(get_inc_dec_mixin(['money'])):
	
	owner_type = models.ForeignKey(ContentType, null = True, blank = True, related_name = 'bond_shares')
	owner_object_id = models.PositiveIntegerField(null = True, blank = True)
	owner = generic.GenericForeignKey('owner_type', 'owner_object_id')
	
	bond = models.ForeignKey(Bond, related_name = 'shares')
	money = DecimalField()
	
	objects = ShareManager()
	
	class Meta:
		ordering = ['-money']