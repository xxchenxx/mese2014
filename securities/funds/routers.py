import views

routes = (
	(r'funds(/(?P<fund_pk>\d+))?/shares', views.ShareAPIViewSet),	
	(r'funds', views.FundAPIViewSet),
)
