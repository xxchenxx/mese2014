from django.contrib import auth
from django.shortcuts import render_to_response
from annoying.decorators import ajax_by_method
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views, generics, mixins, viewsets, permissions, status, renderers
from rest_framework.decorators import action, link, api_view
from rest_framework.response import Response

import models, serializers
import json

class UserAPIViewSet(viewsets.ModelViewSet):
	
	serializer_class = serializers.UserSerializer
	model = auth.models.User
	
	def get_object(self):
		pk = self.kwargs.get('pk', None)
		if pk == 'my':
			return self.request.user
		else:
			return super(UserAPIViewSet, self).get_object()
	
	@action(methods=['GET', 'PATCH'])
	def profile(self, *args, **kwargs):
		profile = self.get_object().profile.info
		serializer = serializers.get_serializer_by_object(profile)(profile, data = self.request.DATA)
		
		if self.request.method == 'GET':
			serializer_class = serializers.get_serializer_by_object(profile)
			return Response(serializer_class(profile).data)
		elif self.request.method == 'PATCH':
			if not serializer.is_valid():
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

			profile = serializer.save(force_update=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
	
@csrf_exempt
def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	
	if request.method == 'GET':
		http_referer = request.META.get('HTTP_REFERER', '/')
		print http_referer
		request.session['referer'] = http_referer
		return render_to_response('accounts/login.html')
	#POST
	
	print request.POST
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	print username,password
	user = auth.authenticate(username = username, password = password)
	print request.session['referer']
	if user is None:
		return HttpResponse('',status=status.HTTP_400_BAD_REQUEST)
	else:
		auth.login(request, user)
		return HttpResponse(json.dumps({'status':'success', 'referer': request.session['referer']}))
		
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
