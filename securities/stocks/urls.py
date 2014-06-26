from django.conf.urls import patterns, include, url

urlpatterns = patterns('securities.stocks.views',
	url('detail/$', 'detail', name='stocks.detail'),
)