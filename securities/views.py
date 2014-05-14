import serializers, models
import logs.models

from rest_framework import viewsets
from common.permissions import IsAdminUser, IsPerson, OwnsObject
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

class FondAPIViewSet(viewsets.ModelViewSet):

	model = models.Fond
	
	#permission_classes = (IsAdminUser,)
	
	def get_serializer_class(self):
		return serializers.get_fond_serializer_class(self.kwargs['fond_type'])
		
	def create(self, *args, **kwargs):
		response = super(FondAPIViewSet, self).create(*args, **kwargs)
		self.object.create_log()
		return response
		
	def get_queryset(self):
		return models.get_fond_class(self.kwargs['fond_type']).objects.all()
	
	@action(methods = ['POST'])
	def buy(self, request, *args, **kwargs):
		self.get_object().buy(self.request.user.profile.info, int(self.request.DATA['quantity']))
		return Response("OK")
		
class LogAPIViewSet(viewsets.ReadOnlyModelViewSet):
	
	model = models.Log
	
	def get_serializer_class(self):
		return serializers.get_log_serializer_class(self.kwargs['fond_type'])
		
	def get_queryset(self):
		print models.get_fond_class(self.kwargs['fond_type'])
		return get_object_or_404(models.get_fond_class(self.kwargs['fond_type']), pk = self.kwargs['fond_pk']).logs.all()
		
class ShareAPIViewSet(viewsets.ReadOnlyModelViewSet):
	
	model = models.Share
	
	permission_classes = (IsPerson, OwnsObject, )
	
	def get_serializer_class(self):
		return serializers.get_share_serializer_class(self.kwargs['fond_type'])
		
	def get_queryset(self):
		return getattr(self.user.profile.info, '%ss_shares' % self.kwargs['fond_type']).all()
		
class TradeLogAPIViewSet(viewsets.ReadOnlyModelViewSet):

	model = logs.models.TradeLog
	serializer_class = serializers.TradeLogSerializer
	permission_classes = (IsPerson, OwnsObject, )
	
	def get_queryset(self):
		return self.request.user.profile.info.trade_logs.all()