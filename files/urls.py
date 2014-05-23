from django.conf.urls import patterns, include, url

urlpatterns = patterns('file_upload.views',
	url(r'^$', 'index'),
)
