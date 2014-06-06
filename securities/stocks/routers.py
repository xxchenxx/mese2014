import views


routes = (
	(r'stocks(/(?P<stock_pk>\d+))?/shares', views.ShareAPIViewSet),
	(r'stocks(/(?P<stock_pk>\d+))?/applications', views.ApplicationAPIViewSet),
	(r'stocks', views.StockAPIViewSet),
)