from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action, api_view

import models, serializers
from accounts.models import Bank
from accounts.serializers import BankSerializer
from django.shortcuts import get_object_or_404
from functools import partial

from decimal import Decimal

@api_view(['POST'])
def transfer(request, *args, **kwargs):
	data = serializers.TransferSerializer(data = request.DATA)
	if data.is_valid():
		data = data.object
		return Response(serializers.TransferLogSerializer(request.user.profile.info.transfer_money(data['to'], data['money'])).data)

class BankAPIViewSet(ReadOnlyModelViewSet):

	model = Bank
	serializer_class = BankSerializer
	
	@action(methods = ['POST'])
	def store(self, request, *args, **kwargs):
		money = Decimal(request.DATA.get('money', 0))
		return Response(serializers.DepositSerializer(request.user.profile.info.store_money(self.get_object(), money)).data)
		
	@action(methods = ['POST'])
	def remove(self, request, *args, **kwargs):
		money = Decimal(request.DATA.get('money', 0))
		return Response(serializers.DepositSerializer(request.user.profile.info.remove_money(self.get_object(), money)).data)

class TransferLogAPIViewSet(ReadOnlyModelViewSet):

	model = models.TransferLog
	serializer_class = serializers.TransferLogSerializer

class DepositAPIViewSet(ReadOnlyModelViewSet):

	model = models.Deposit
	serializer_class = serializers.DepositSerializer
	
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
