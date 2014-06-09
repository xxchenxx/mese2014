from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
	url(r'^login/$', 'login', name = 'accounts.login'),
	url(r'^logout/$', 'logout', name = 'accounts.logout'),
	url(r'^profile/$', 'profile', name = 'accounts.profile'),
)
