from django.conf.urls import patterns, include, url
import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'passages', views.PassageViewSet)

urlpatterns = patterns('webboard.views',
	url(r'^', include(router.urls)),
)