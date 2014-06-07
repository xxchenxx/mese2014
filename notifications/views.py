from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, ListModelMixin
import models, serializers

class NotificationAPIViewSet(GenericViewSet, DestroyModelMixin, RetrieveModelMixin, ListModelMixin):
	
	model = models.Notification
	serializer_class = serializers.NotificationSerializer
	
	def get_queryset(self):
		return self.request.user.notifications.all()
