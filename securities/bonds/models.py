from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField

class Bond(models.Model):
	
	display_name = models.CharField(max_length = 255, default = '')
	
	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	
	published = models.BooleanField(default = False)
	
	interest_rate = DecimalField()
	lasted_time = models.TimeField()
	published_time = models.DateTimeField()
	created_time = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		ordering = ['-created_time']
	
class Share(models.Model):
	
	owner_type = models.ForeignKey(ContentType, null = True, blank = True, related_name = 'bond_shares')
	owner_object_id = models.PositiveIntegerField(null = True, blank = True)
	owner = generic.GenericForeignKey('owner_type', 'owner_object_id')
	
	bond = models.ForeignKey(Bond, related_name = 'shares')
	money = DecimalField()
	
	class Meta:
		ordering = ['-money']