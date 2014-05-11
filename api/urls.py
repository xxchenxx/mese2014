from django.conf.urls import url, patterns, include

from rest_framework.routers import DefaultRouter

from webboard.views import PassageAPIViewSet, CommentAPIViewSet
from accounts.views import UserAPIViewSet
from file_upload.views import PrivateFileAPIViewSet, PublicFileAPIViewSet
from securities.views import ShareAPIViewSet, FondAPIViewSet, LogAPIViewSet, TradeLogAPIViewSet

router = DefaultRouter()
router.register(r'passages', PassageAPIViewSet)
router.register(r'passages/(?P<passage_pk>\d+)/comments', CommentAPIViewSet)
router.register(r'users', UserAPIViewSet)
router.register(r'files/public', PublicFileAPIViewSet)
router.register(r'files/private', PrivateFileAPIViewSet)
router.register(r'(?P<fond_type>bond|future|fund|stock)s', FondAPIViewSet)
router.register(r'(?P<fond_type>bond|future|fund|stock)s/(?P<fond_pk>\d+)/logs', LogAPIViewSet)
router.register(r'(?P<fond_type>bond|future|fund|stock)s/shares', ShareAPIViewSet)
router.register(r'trade-logs/', TradeLogAPIViewSet)

urlpatterns = patterns('',
	url(r'^auth/', include('rest_framework.urls', namespace = 'rest_framework')),
	url(r'^', include(router.urls)),
)