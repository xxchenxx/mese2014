from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
import models, serializers
from accounts.models import filter_accounts, account_classes_map
from common.permissions import IsAdminUser
from .exceptions import ParamError
from decimal import Decimal
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from common.permissions import IsSubClass

class LogAPIViewSet(GenericViewSet, mixins.ListModelMixin):
	
	model = models.Log
	serializer_class = serializers.LogSerializer
	
	def get_queryset(self):
		pk = self.kwargs.get('stock_pk', None)
		stock = get_object_or_404(models.Stock, pk = pk)
		return stock.logs.all()

class ShareAPIViewSet(GenericViewSet, mixins.ListModelMixin):
	
	model = models.Share
	serializer_class = serializers.ShareSerializer
	permission_classes = [IsSubClass('HasStockMixin')]
	
	def get_queryset(self):
		stock_pk = self.kwargs.get('stock_pk', None)
		qs = self.request.user.profile.info.stock_shares.all()
		if stock_pk is not None:
			qs = qs.filter(stock_id = stock_pk)
		return qs
		
class ApplicationAPIViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
	
	model = models.Application
	serializer_class = serializers.ApplicationSerializer
	permission_classes = [IsSubClass('HasStockMixin')]
	
	def get_queryset(self):
		stock_pk = self.kwargs.get('stock_pk', None)
		qs = self.request.user.profile.info.stock_applications.all()
		if stock_pk is not None:
			qs = qs.filter(stock_id = stock_pk)
			
		return qs

class StockAPIViewSet(ModelViewSet):
	
	serializer_class = serializers.StockSerializer
	model = models.Stock
	#permission_classes = (IsAdminUser,)
	
	def create(self, request, *args, **kwargs):
		owner = request.DATA.pop('owner', None)
		if owner is None or not isinstance(owner, (int, str, unicode)):
			raise ParamError("The owner field must be set or it must be the ID or display_name")
		
		shares = request.DATA.pop('shares', None)
		owner = filter_accounts(display_name = owner)[0]
		owner = account_classes_map[owner['account_type']](id = owner['id'])
		
		response = super(StockAPIViewSet, self).create(request, *args, **kwargs)
		models.Share.objects.create(stock = self.object, shares = shares, owner = owner)
		return response	
		
	def apply(self, request, type, *args, **kwargs):
		price = request.DATA.get('price', None)
		shares = request.DATA.get('shares', None)
		if price is None or shares is None:
			raise ParamError("Shares and money must be set.")
		shares = Decimal(shares)
		price = Decimal(price)
		res = request.user.profile.info._apply(type, self.get_object(), price, shares)
			
		return Response(serializers.ApplicationSerializer(res).data)		
		
	@action(methods = ['POST'],permission_classes = [IsSubClass('HasStockMixin')])
	def buy(self, request, *args, **kwargs):
		return self.apply(request, models.Application.BUY, *args, **kwargs)
		
	@action(methods = ['POST'],permission_classes = [IsSubClass('HasStockMixin')])
	def sell(self, request, *args, **kwargs):
		return self.apply(request, models.Application.SELL, *args, **kwargs)
