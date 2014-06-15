#encoding=utf8
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
	
	def create_notifications(self, instances = []):
		objects = []
		for data in instances:
			objects.append(self._create(**data))
			
		return self.bulk_create(objects)
	
	def _create(self, recipient, verb, fmt = None, actor = None, target = None, url = None, action = None):
		obj = Notification(recipient = recipient, verb = verb)
		obj.actor = actor
		obj.target = target
		print actor, target, verb
		if fmt is None:
			fmt = u'%(actor)s%(verb)s'
			if obj.target is not None:
				fmt+=u'%(target)s'
			
		obj.message = fmt % {'actor': obj.actor, 'target': obj.target, 'verb': obj.verb}
		if obj.target_object and url is None:
			try:
				obj.url = obj.target_object.get_absolute_url()
			except AttributeError:
				obj.url = ''
		elif url is not None:
			obj.url = url
		
		if action is not None:
			obj.action = action
		
		return obj
		
	def create_notification(self, **kwargs):
		obj = self._create(**kwargs)
		obj.save()
		return obj
		
class NotificationManager(managers.PassThroughManager):
	pass
		
class Notification(models.Model):

	recipient = models.ForeignKey(
			'auth.User', 
			related_name = 'notifications'
	)
	unread = models.BooleanField(default = True)
	confirmed = models.BooleanField(default = False)
	
	DELETE = 'delete'
	NULL = 'null'
	ACTION_CHOICES = (
		(DELETE, 'delete'),
		(NULL, 'null'),
	)
	
	actor_text = models.CharField(max_length=255, blank=True, null=True)
	actor_content_type = models.ForeignKey(ContentType, related_name='notify_actor', blank = True, null = True)
	actor_object_id = models.CharField(max_length=255, blank = True, null = True)
	actor_object = generic.GenericForeignKey('actor_content_type', 'actor_object_id')
	
	verb = models.CharField(max_length=255)
	
	target_text = models.CharField(max_length=255, blank=True, null=True)
	target_content_type = models.ForeignKey(ContentType, related_name='notify_target',
		blank=True, null=True)
	target_object_id = models.CharField(max_length=255, blank=True, null=True)
	target_object = generic.GenericForeignKey('target_content_type',
		'target_object_id')
		
	created_time = models.DateTimeField(auto_now_add = True)
	
	message = models.TextField()
	
	url = models.URLField(max_length=255, null=True, blank = True)
	
	action = models.CharField(max_length=30, choices = ACTION_CHOICES, default = NULL, blank = True)
	
	objects = NotificationManager.for_queryset_class(NotificationQuerySet)()
	
	class Meta:
		ordering = ['-created_time']
		
	def confirm(self):
		self.confirmed = True
		self.save()
		if self.action == self.DELETE:
			self.target_object.delete()
		
	@property
	def actor(self):
		if self.actor_object is not None:
			return self.actor_object
		else:
			return self.actor_text
			
	@property
	def target(self):
		if self.target_object is not None:
			return self.target_object
		else:
			return self.target_text
			
	@actor.setter
	def actor(self, value):
		if isinstance(value, (str, unicode)):
			self.actor_text = value
		else:
			self.actor_object = value
			
	@target.setter
	def target(self, value):
		if isinstance(value, (str, unicode)):
			self.target_text = value
		else:
			self.target_object = value	
		
print Notification.objects
