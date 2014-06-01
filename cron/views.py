# Create your views here.
from django.http import HttpResponse
from .cron import cache

def index(request):
	crons = cache.get_crons()
	return HttpResponse('')