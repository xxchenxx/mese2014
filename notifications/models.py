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
		
	def process_message(self, verb, actor = None, target = None, **kwargs):
		_actor = u'有人' if actor is None else actor
		if target is None:
			msg = u"%s %s" % (_actor, verb)
		else:
			msg = u"%s %s %s" % (_actor, verb, target)
			
		return msg		
	
	def create_notifications(self, instances = []):
		objects = []
		for data in instances:
			msg = self.process_message(**data)
			data['message'] = msg
			if 'actor' in data and (not data['actor'] or isinstance(data['actor'], (unicode,str))):
				data.pop('actor')
			if 'target' in data and (not data['target'] or isinstance(data['target'], (unicode,str))):
				data.pop('target')
			objects.append(Notification(**data))
			
		return self.bulk_create(objects)
	
	def create_notification(self, recipient, verb, actor = None, target = None):
		msg = self.process_message(verb, actor, target)
		print msg
		args = {
			'recipient': recipient,
			'verb': verb,
			'actor': actor,
			'target': target,
			'message': msg,
		}
		if not args['actor'] or isinstance(actor, (str, unicode)):
			args.pop('actor')
		if not args['target'] or isinstance(target, (str, unicode)):
			args.pop('target')
		return self.create(**args)
		
class NotificationManager(managers.PassThroughManager):
	pass
		
class Notification(models.Model):

	recipient = models.ForeignKey(
			'auth.User', 
			related_name = 'notifications'
	)
	unread = models.BooleanField(default = True)
	
	actor_content_type = models.ForeignKey(ContentType, related_name='notify_actor', blank = True, null = True)
	actor_object_id = models.CharField(max_length=255, blank = True, null = True)
	actor = generic.GenericForeignKey('actor_content_type', 'actor_object_id')
	
	verb = models.CharField(max_length=255)
	
	target_content_type = models.ForeignKey(ContentType, related_name='notify_target',
		blank=True, null=True)
	target_object_id = models.CharField(max_length=255, blank=True, null=True)
	target = generic.GenericForeignKey('target_content_type',
		'target_object_id')
		
	created_time = models.DateTimeField(auto_now_add = True)
	
	message = models.TextField()
	
	objects = NotificationManager.for_queryset_class(NotificationQuerySet)()
	
	class Meta:
		ordering = ['-created_time']
		
print Notification.objects
