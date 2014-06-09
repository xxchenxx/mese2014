from common.mixins import *

__all__ = ['CanWriteMixin']

class CanWriteMixin(models.Model):

	class Meta:
		abstract = True
