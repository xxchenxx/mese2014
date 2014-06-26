from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action, api_view, permission_classes

import models, serializers
from common.permissions import IsSubClass
from accounts.models import Bank
from accounts.serializers import BankSerializer
from django.shortcuts import get_object_or_404
from functools import partial

from decimal import Decimal
from captcha.decorators import check_captcha

@api_view(['POST'])
@permission_classes([IsSubClass('CanTransferMixin')])
@check_captcha()
def transfer(request, *args, **kwargs):
	data = serializers.TransferSerializer(data = request.DATA)
	if data.is_valid():
		data = data.object
		return Response(serializers.TransferLogSerializer(request.user.profile.info.transfer_money(data['to'], data['money'])).data)
	else:
		return Response(data.errors, status = status.HTTP_400_BAD_REQUEST)

class BankAPIViewSet(ReadOnlyModelViewSet):

	model = Bank
	serializer_class = BankSerializer
	
	@action(methods = ['POST'], permission_classes = [IsSubClass('CanStoreMixin')])
	def store(self, request, *args, **kwargs):
		money = Decimal(request.DATA.get('money', 0))
		return Response(serializers.DepositSerializer(request.user.profile.info.store_money(self.get_object(), money)).data)
		
	@action(methods = ['POST'], permission_classes = [IsSubClass('CanStoreMixin')])
	def remove(self, request, *args, **kwargs):
		money = Decimal(request.DATA.get('money', 0))
		return Response(serializers.DepositSerializer(request.user.profile.info.remove_money(self.get_object(), money)).data)

class TransferLogAPIViewSet(ReadOnlyModelViewSet):

	model = models.TransferLog
	serializer_class = serializers.TransferLogSerializer
	permission_classes = (IsSubClass('CanTransferMixin'),)

class DepositAPIViewSet(ReadOnlyModelViewSet):

	model = models.Deposit
	serializer_class = serializers.DepositSerializer
	permission_classes = (IsSubClass('CanStoreMixin'),)
	
	def get_serializer_class(self):
		pk = self.kwargs.get('bank_pk', None)
		cls = serializers.DepositSerializer
		if pk is not None:
			cls = partial(cls, exclude = ['bank'])
			
		return cls
	
	def get_queryset(self):
		qs = self.request.user.profile.info.deposits.all()
		pk = self.kwargs.get('bank_pk', None)
		if pk is not None:
			qs = qs.filter(bank_id = pk)
			
		return qs
