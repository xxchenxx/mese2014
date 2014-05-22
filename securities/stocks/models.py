from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Stock(models.Model):
	
	publisher_type = models.ForeignKey(ContentType, null = True, blank = True)
	publisher_object_id = models.PositiveIntegerField(null = True, blank = True)
	publisher = generic.GenericForeignKey('publisher_type', 'publisher_object_id')
	
class Log(models.Model):
	
	stock = models.ForeignKey(Stock, related_name = 'logs')

class Application(models.Model):

	applicant_type = models.ForeignKey(ContentType, null = True, blank = True)
	applicant_object_id = models.PositiveIntegerField(null = True, blank = True)
	applicant = generic.GenericForeignKey('applicant_type', 'applicant_object_id')
	
	stock = models.ForeignKey(Stock, related_name = 'applications')
	
class Share(models.Model):
	
	owner_type = models.ForeignKey(ContentType, null = True, blank = True)
	owner_object_id = models.PositiveIntegerField(null = True, blank = True)
	owner = generic.GenericForeignKey('owner_type', 'owner_object_id')
	
	stock = models.ForeignKey(Stock, related_name = 'applications')