from models import File
from annoying.decorators import ajax_request, render_to
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import DefaultStorage
from django.conf import settings

@render_to('upload_test.html')
def index(request):
	return {}
	
@ajax_request
@csrf_exempt
def upload_view(request):
	file_type = request.POST.get('type', 'public').lower()
	saved_in_db = request.POST.get('saved', '')
	file = request.FILES['Filedata']
	
	return_value = {'name': file.name}
	if saved_in_db:
		id  = File.objects.create(file_type = file_type, file = file).id
		return_value.update({'id':id})
	else:
		storage = DefaultStorage()
		return_value.update({'url': storage.url(storage.save(file.name, file))})
	return return_value