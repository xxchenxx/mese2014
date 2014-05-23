from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField

class Fund(models.Model):

	OPEN = 'open'
	CLOSE = 'close'
	TYPE_CHOICE = (
		(OPEN, 'open'),
		(CLOSE, 'close'),
	)

	display_name = models.CharField(max_length = 255, default = '')

	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	
	account = models.OneToOneField('accounts.Fund', related_name = 'fund', null = True, blank = True)
	
	published = models.BooleanField(default = False)
	
	min_return_rate = DecimalField()
	max_return_rate = DecimalField()
	inital_money = DecimalField()
	lasted_time = DecimalField()
	published_time = DecimalField()
	
	fund_type = models.CharField(max_length = 10, choices = TYPE_CHOICE)
	
	created_time = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		ordering = ['-created_time']
	
class ClosedEndFund(Fund):
	
	class Meta:
		proxy = True
	
class OpenEndFund(Fund):

	class Meta:
		proxy = True
		
class Share(models.Model):

	owner_type = models.ForeignKey(ContentType, null = True, blank = True, related_name = 'fund_shares')
	owner_object_id = models.PositiveIntegerField(null = True, blank = True)
	owner = generic.GenericForeignKey('owner_type', 'owner_object_id')
	
	fund = models.ForeignKey(Fund, related_name = 'shares')
	money = DecimalField()
	
	class Meta:
		ordering = ['-money']