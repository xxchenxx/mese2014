from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Bond(models.Model):
	
	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	
class Log(models.Model):
	
	bond = models.ForeignKey(Bond, related_name = 'logs')
	
class Share(models.Model):
	
	pass