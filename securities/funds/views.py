from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
import models, serializers
from common.exceptions import *
from decimal import Decimal

class ShareAPIViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
	
	model = models.Share
	serializer_class = serializers.ShareSerializer
	
	def get_queryset(self):
		fund_pk = self.kwargs.get('fund_pk', None)
		qs = self.request.user.profile.info.fund_shares.all()
		if fund_pk is not None:
			qs = qs.filter(fund_id = fund_pk)
			
		return qs
		
class FundAPIViewSet(ModelViewSet):

	model = models.Fund
	serializer_class = serializers.FundSerializer
	
	@action(methods = ['POST'])
	def buy(self, request, *args, **kwargs):
		money = request.DATA.get('money', None)
		if money is None:
			raise ParamError("The field `money` must be set.")
			
		account = request.user.profile.info
		account.buy_fund(self.get_object(), Decimal(money))
		return Response('OK', status = status.HTTP_200_OK)