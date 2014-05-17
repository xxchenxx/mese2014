from models import File, PublicFile, PrivateFile
from serializers import PublicFileSerializer, PrivateFileSerializer

from annoying.decorators import ajax_request, render_to
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import DefaultStorage
from django.conf import settings
 
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from common.permissions import HasReport, IsAdminUser, HasFile

from django.http import Http404

@render_to('upload_test.html')
def index(request):
	return {}
	
@ajax_request
@csrf_exempt
def upload_view(request):
	file = request.FILES['file']
	
	return_value={}
	
	storage = DefaultStorage()
	return_value.update({'url': storage.url(storage.save(file.name, file))})
	return return_value

class PublicFileAPIViewSet(ModelViewSet):

	model = PublicFile
	serializer_class = PublicFileSerializer
	permission_classes = (IsAdminUser, )
	
	def create(self, request, *args, **kwargs):
		request.DATA['file_type'] = File.PUBLIC
		return super(PublicFileAPIViewSet, self).create(request, *args, **kwargs)	
	
class PrivateFileAPIViewSet(ModelViewSet):
	
	model = PrivateFile
	serializer_class = PrivateFileSerializer
	permission_classes = (HasReport,)
	
	def dispatch(self, request, *args, **kwargs):
		self.account = request.user.profile.info
		self.field_name = (kwargs['field_name'] or self.account.report_field).replace('-','_')
		print self.field_name
		field = self.account.has_field(self.field_name)
		if self.field_name:
			if not field:
				raise Http404
		return super(PrivateFileAPIViewSet, self).dispatch(request, *args, **kwargs)
	
	def get_queryset(self):
		return getattr(self.account, self.field_name).all()
	
	def get_object(self, *args, **kwargs):
		return super(PrivateFileAPIViewSet, self).get_object(*args, **kwargs)
	
	def create(self, request, *args, **kwargs):
		request.DATA['file_type'] = File.PRIVATE
		response = super(PrivateFileAPIViewSet, self).create(request, *args, **kwargs)
		self.request.user.profile.info.upload_reports(self.object,field_name = self.field_name)
		return response