from rest_framework import serializers
from .models import TransferLog, Deposit
from accounts.serializers import BankSerializer, AccountField

class TransferSerializer(serializers.Serializer):
	
	to = AccountField()
	money = serializers.DecimalField()

	def restore_object(self, attrs, instance = None):
		return {
			'to': attrs.get('to'),
			'money': attrs.get('money')
			}
class TransferLogSerializer(serializers.ModelSerializer):
	
	transfer_by = AccountField(required = False)
	transfer_to = AccountField(required = False)	
	
	class Meta:
		model = TransferLog
		fields = ('transfer_by', 'transfer_to', 'money', 'created_time')

class DepositSerializer(serializers.ModelSerializer):

	bank = BankSerializer()

	class Meta:
		model = Deposit
		fields = ('bank', 'money')
