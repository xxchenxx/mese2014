# Create your views here.
from django.http import HttpResponse
from .core import cache
import memcache, datetime

cache_client = memcache.Client()

def index(request):
	crons = cache.get_crons()
	print crons
	times = cache_client.get_multi(crons.keys())
	for cron_name, cron_cls in crons.iteritems():
		cron = cron_cls()
		if cron.execute(times.get(cron_name, None)):
			cache_client.set(cron_name, datetime.datetime.now())
	
	return HttpResponse('')