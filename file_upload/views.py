from models import File, PublicFile, PrivateFile
from serializers import PublicFileSerializer, PrivateFileSerializer

from annoying.decorators import ajax_request, render_to
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import DefaultStorage
from django.conf import settings
 
from rest_framework.viewsets import ModelViewSet
from common.permissions import HasReport, IsAdminUser, HasFile

@render_to('upload_test.html')
def index(request):
	return {}
	
@ajax_request
@csrf_exempt
def upload_view(request):
	# file_type = request.POST.get('type', 'public').lower()
	# saved_in_db = request.POST.get('saved', '')
	file = request.FILES['Filedata']
	
	# return_value = {'name': file.name}
	# if saved_in_db:
		# id  = File.objects.create(file_type = file_type, file = file).id
		# return_value.update({'id':id})
	# else:
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
	permission_classes = (HasReport, HasFile)
	
	def get_queryset(self):
		account = self.request.user.profile.info
		return getattr(account, account.report_field).all()
		
	def create(self, request, *args, **kwargs):
		request.DATA['file_type'] = File.PRIVATE
		response = super(PrivateFileAPIViewSet, self).create(request, *args, **kwargs)
		self.request.user.profile.info.upload_reports(self.object.pk)
		return response