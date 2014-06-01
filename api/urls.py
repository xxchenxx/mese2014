from django.conf.urls import url, patterns, include

from rest_framework.routers import DefaultRouter

from webboard.views import PassageAPIViewSet, CommentAPIViewSet
from accounts.views import UserAPIViewSet
from files.views import PrivateFileAPIViewSet, PublicFileAPIViewSet
from timeline.views import TimelineAPIView

router = DefaultRouter()
router.register(r'passages', PassageAPIViewSet)
router.register(r'passages/(?P<passage_pk>\d+)/comments', CommentAPIViewSet)
router.register(r'users', UserAPIViewSet)
router.register(r'files/public', PublicFileAPIViewSet)

urlpatterns = patterns('',
	url(r'^auth/', include('rest_framework.urls', namespace = 'rest_framework')),
	url(r'^timeline/$', TimelineAPIView.as_view()),
	url(r'^files/$',	'files.views.upload_view'),
	url(r'^', include(router.urls)),
)