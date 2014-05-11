import serializers, models

from rest_framework import viewsets
from common.permissions import IsAdminUser, IsPerson, OwnsObject
from rest_framework.generics import get_object_or_404

class FondAPIViewSet(viewsets.ModelViewSet):

	model = models.Fond
	
	permission_classes = (IsAdminUser,)
	
	def get_serializer_class(self):
		return serializers.get_fond_serializer_class(self.kwargs['fond_type'])
		
	def get_queryset(self):
		return models.get_fond_class(self.kwargs['fond_type']).objects.all()
		
class LogAPIViewSet(viewsets.ReadOnlyModelViewSet):
	
	model = models.Log
	
	def get_serializer_class(self):
		return serializers.get_log_serializer_class(self.kwargs['fond_type'])
		
	def get_queryset(self):
		return get_object_or_404(models.get_fond_class(self.kwargs['fond_type']), pk = self.kwargs['fond_pk']).logs.all()
		
class ShareAPIViewSet(viewsets.ReadOnlyModelViewSet):
	
	model = models.Share
	
	permission_classes = (IsPerson, OwnsObject, )
	
	def get_serializer_class(self):
		return serializers.get_share_serializer_class(self.kwargs['fond_type'])
		
	def get_queryset(self):
		return getattr(self.user.profile.info, '%ss_shares' % self.kwargs['fond_type']).all()