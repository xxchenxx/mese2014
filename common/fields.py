from functools import partial
from django.db import models

DecimalField = partial(
		models.DecimalField,
		max_digits = 15,
		decimal_places = 4,
		default = 0
)