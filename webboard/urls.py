from django.conf.urls import patterns, include, url
import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'passages', views.PassageRetrieveViewSet)
router.register(r'api/passages', views.PassageUpdateViewSet)

urlpatterns = patterns('webboard.views',
	url(r'^', include(router.urls)),
)