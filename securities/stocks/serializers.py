from rest_framework import serializers
from .models import Stock, Share, Application

class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock