import views

routes = (
		(r'banks(/(?P<bank_pk>\d+))?/deposits', views.DepositAPIViewSet),
		(r'banks', views.BankAPIViewSet),
		(r'transfer/$', views.transfer),
		(r'transfer/logs', views.TransferLogAPIViewSet),
)
