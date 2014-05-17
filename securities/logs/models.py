from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from common.fields import DecimalField
from timeline.fields import FinancialYearField

class TradeLog(models.Model):

	ACTION_TYPE = (
		('buy', 'buy'),
		('sell', 'sell'),
	)

	owner = models.ForeignKey('accounts.Person', related_name = 'trade_logs')
	action = models.CharField(max_length = 4, choices = ACTION_TYPE, editable = False)
	
	fond_type = models.ForeignKey(ContentType)
	fond_object_id = models.PositiveIntegerField()
	fond = generic.GenericForeignKey('fond_type', 'fond_object_id')
	
	quantity = DecimalField()
	money = DecimalField()
	
	operated_time = models.DateTimeField(auto_now_add = True)
	year = FinancialYearField()
	
	class Meta:
		ordering = ['operated_time']