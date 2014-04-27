from functools import partial
from django.db import models

DecimalField = partial(
		models.DecimalField,
		max_digits = 4,
		decimal_places = 2,
		default = 0
)