from django.conf.urls import url, patterns, include

from rest_framework.routers import DefaultRouter

from webboard.views import PassageAPIViewSet, CommentAPIViewSet
from accounts.views import UserAPIViewSet

router = DefaultRouter()
router.register(r'webboard/passages', PassageAPIViewSet)
router.register(r'webboard/passages/(?P<passage_pk>\d+)/comments', CommentAPIViewSet)
router.register(r'accounts/users', UserAPIViewSet)

urlpatterns = patterns('',
	url(r'^', include(router.urls))
)