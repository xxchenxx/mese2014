from .models import Notification

def send_notifications(data):
	return Notification.objects.create_notifications(data)

def send_notification(recipient, verb, actor = None, target = None):
	return Notification.objects.create_notification(recipient, verb, actor, target)
