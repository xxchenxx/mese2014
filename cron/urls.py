from django.conf.urls import patterns, url, include

urlpatterns = patterns('cron.views',
  url('^$', 'index'),
)