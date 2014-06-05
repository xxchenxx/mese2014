from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
import models, serializers
from accounts.models import filter_accounts, account_classes_map
from common.permissions import IsAdminUser
from .exceptions import ParamError
from decimal import Decimal
from rest_framework.response import Response

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
		owner = account_classes_map[owner.account_type](id = owner.id)
		
		response = super(StockAPIViewSet, self).create(request, *args, **kwargs)
		Share.objects.create(stock = self.object, shares = shares, owner = owner)
		return response
		
	@action(methods = ['POST'])
	def buy(self, request, *args, **kwargs):
		price = request.DATA.pop('price', None)
		shares = request.DATA.pop('shares', None)
		if price is None or shares is None:
			raise ParamError("Shares and money must be set.")
		shares = Decimal(shares)
		price = Decimal(price)
			
		return Response(serializers.ApplicationSerializer(request.user.profile.info.buy_stock(self.get_object(), price, shares)).data)
		
	@action(methods = ['POST'])
	def sell(self, request, *args, **kwargs):
		price = request.DATA.pop('price', None)
		shares = request.DATA.pop('shares', None)
		if shares is None or price is None:
			raise ParamError("Shares and money must be set.")
		shares = Decimal(shares)
		price = Decimal(price)
			
		return Response(serializers.ApplicationSerializer(request.user.profile.info.sell_stock(self.get_object(), price, shares)).data)