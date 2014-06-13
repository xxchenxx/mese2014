from .models import Notification

def send_notifications(data):
	return Notification.objects.create_notifications(data)

def send_notification(**kwargs):
	return Notification.objects.create_notification(**kwargs)
