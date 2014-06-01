from django.db import models

from common.fields import DecimalField

class Future(models.Model):
	
	display_name = models.CharField(max_length = 30, default = '')
	current_price = DecimalField()