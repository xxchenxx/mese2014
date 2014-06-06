from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from model_utils import managers

class NotificationQuerySet(models.query.QuerySet):
	
	def unread(self):
		return self.filter(unread = True)
		
	def read(self):
		return self.filter(unread = False)
		
	def mark_all_as_read(self, recipient=None):
		qs = self.unread()
		if recipient:
			qs = qs.filter(recipient=recipient)
		
		qs.update(unread=False)
	
	def mark_all_as_unread(self, recipient=None):
		qs = self.read()
		
		if recipient:
			qs = qs.filter(recipient=recipient)
			
		qs.update(unread=True)
		
class Notification(models.Model):

	recipient = models.ForeignKey(
			'auth.User', 
			related_name = 'notifications'
	)
	unread = models.BooleanField(default = True)
	
	actor_content_type = models.ForeignKey(ContentType, related_name='notify_actor')
	actor_object_id = models.CharField(max_length=255)
	actor = generic.GenericForeignKey('actor_content_type', 'actor_object_id')
	
	verb = models.CharField(max_length=255)
	
	target_content_type = models.ForeignKey(ContentType, related_name='notify_target',
		blank=True, null=True)
	target_object_id = models.CharField(max_length=255, blank=True, null=True)
	target = generic.GenericForeignKey('target_content_type',
		'target_object_id')
		
	created_time = models.DateTimeField(auto_now_add = True)
	
	objects = managers.PassThroughManager.for_queryset_class(NotificationQuerySet)()
	
	class Meta:
		ordering = ['-created_time']