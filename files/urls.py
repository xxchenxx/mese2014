from django.conf.urls import patterns, include, url

urlpatterns = patterns('files.views',
	url(r'^$', 'index'),
)
