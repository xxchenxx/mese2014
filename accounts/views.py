from django.contrib import auth
from django.shortcuts import render_to_response
from annoying.decorators import ajax_by_method
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views, generics, mixins, viewsets, permissions, response, status, renderers
from rest_framework.decorators import action, link
import models, serializers

class UserViewSet(viewsets.ModelViewSet):
	
	serializer_class = serializers.UserSerializer
	model = auth.models.User

@ajax_by_method('accounts/login.html')
@csrf_exempt
def login(request):
	http_referer = request.META.get('HTTP_REFERER', '/')
	if request.user.is_authenticated():
		return HttpResponseRedirect(http_referer)
	
	request.session['referer'] = http_referer
	if request.method == 'GET':
		return {}
	#POST
	
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username = username, password = password)
	if user is None:
		return {'status':'error'}
	else:
		auth.login(request, user)
		return {'status':'success', 'referer': request.session['referer']}
		
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')