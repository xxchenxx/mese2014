from django.conf.urls import patterns, include, url

urlpatterns = patterns('securities.views',
	url(r'^$', 'index'),
)