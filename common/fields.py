from functools import partial
from django.db import models
from timeline.fields import FinancialYearField
from datetime import timedelta

DecimalField = partial(
		models.DecimalField,
		max_digits = 15,
		decimal_places = 4,
		default = 0
)

class TimeDeltaField(models.PositiveIntegerField):

	descrption = "datetime.timedelta"
	
	def get_prep_value(self, value):
		if isinstance(value, timedelta):
			return int(value.total_seconds())
			
		return super(TimeDeltaField, self).get_prep_value(value)
		
	def to_python(self, value):
		return timedelta(seconds = value)