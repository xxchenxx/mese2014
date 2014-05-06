from django.conf.urls import patterns, include, url
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('accounts.views',
	url(r'^login/$', 'login', name = 'accounts.login'),
	url(r'^logout/$', 'logout', name = 'accounts.logout'),
	url(r'^', include(router.urls)),
)