from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
import models, serializers
from common.exceptions import *
from decimal import Decimal
from .permissions import *

class ShareAPIViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
	
	model = models.Share
	serializer_class = serializers.ShareSerializer
	permission_classes = [HasBond, HasBondShare]
	
	def get_queryset(self):
		bond_pk = self.kwargs.get('bond_pk', None)
		qs = self.request.user.profile.info.bond_shares.all()
		if bond_pk is not None:
			qs = qs.filter(bond_id = bond_pk)
			
		return qs
		
class BondAPIViewSet(ModelViewSet):

	model = models.Bond
	serializer_class = serializers.BondSerializer
	
	@action(methods = ['GET'], permission_classes = [HasBondObject, OwnBond])
	def ransom(self, request, *args, **kwargs):
		self.get_object().ransom()
		return Response('OK', status = status.HTTP_200_OK)
		
	@action(methods = ['POST'], permission_classes = [HasBond])
	def buy(self, request, *args, **kwargs):
		money = request.DATA.get('money', None)
		if money is None:
			raise ParamError("The field `money` must be set.")
			
		account = request.user.profile.info
		account.buy_bond(self.get_object(), Decimal(money))
		return Response('OK', status = status.HTTP_200_OK)
