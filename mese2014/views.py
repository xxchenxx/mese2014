from annoying.decorators import render_to
from django.http import HttpResponse
@render_to("index.html")
def index(request):
	return {}
	
def cron(request):
	print 1
	return HttpResponse()