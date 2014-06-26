#encoding=utf8
from django.db import models
from django.db.models import F

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField, TimeDeltaField
from common.mixins import get_inc_dec_mixin
from exceptions import BondPublished

from decimal import Decimal

from django.core.exceptions import ValidationError
from django.conf import settings
from notifications import send_notification

class BondManager(models.Manager):
	
	def published(self):
		return self.filter(published = True)

class Bond(models.Model):
	
	GOVERNMENT = 'GOV'
	ENTERPRISE = 'ENT'
	TYPE_CHOICE = (
			(GOVERNMENT, 'Government'),
			(ENTERPRISE, 'Enterprise'),
	)
	
	display_name = models.CharField(max_length = 255, default = '', blank = True)
	
	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	type = models.CharField(max_length = 3, choices = TYPE_CHOICE)
	
	published = models.BooleanField(default = False)
	
	profit_rate = DecimalField()
	lasted_time = TimeDeltaField()
	published_time = models.DateTimeField()
	created_time = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		if self.type == self.GOVERNMENT:
			_type = u'政府'
		else:
			_type = u'公司'
			
		return u'%s债券 %s' % (_type, self.display_name)
	
	def publish(self):
		self.published = True
		self.save()
		send_notification(recipient = self.publisher.profile.user, verb = u'已经发布了', actor = self, target = self) 
		
	def check_published(self):
		if self.published:
			raise BondPublished
	
	def finish(self, times = 1):
		rate = self.profit_rate / 100
		total = Decimal(0)
		shares = self.shares.prefetch_related()
		for share in shares:
			money = share.money * (1+rate) ** times
			total += money
			share.owner.inc_assets(money)
		if self.type == self.ENTERPRISE:
			self.publisher.dec_assets(total)
		send_notification(recipient = self.publisher.profile.user, verb = u'已经结束了', actor = self) 
		shares.delete()
		self.delete()
	
	def ransom(self):
		if not self.published:
			raise ValidationError("The bond hasn't been published.")
		times = self.lasted_time // (5*60)+1
		self.finish(times)
	
	def share_profits(self):
		rate = self.profit_rate / 100
		total = Decimal(0)
		for share in self.shares.prefetch_related():
			money = share.money * rate
			total += money
			share.owner.inc_assets(money)
		if self.type == self.ENTERPRISE:
			self.publisher.dec_assets(total)
	
	def clean_fields(self, *args, **kwargs):
		if not self.type:
			self.type = self.GOVERNMENT if self.publisher.__class__.__name__ == 'Government' else self.ENTERPRISE
			
		super(Bond, self).clean_fields(*args, **kwargs)
	
	def apply_money(self, actor, money):
		share = actor.get_bond_share(self, create = True, money = money).inc_money(money)
		self.publisher.inc_assets(money)
	
	class Meta:
		ordering = ['-created_time']
		permissions = (
			('has_bond', 'Has bond'),
			('own_bond', 'Own bond'),
		)
		
	objects = BondManager()
	
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
