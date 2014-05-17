from functools import partial
from django.db import models
from timeline.fields import FinancialYearField

DecimalField = partial(
		models.DecimalField,
		max_digits = 15,
		decimal_places = 4,
		default = 0
)