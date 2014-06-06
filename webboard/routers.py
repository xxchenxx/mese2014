import views

routes = (
	(r'passages', views.PassageAPIViewSet),
	(r'passages/(?P<passage_pk>\d+)/comments', views.CommentAPIViewSet),
	)