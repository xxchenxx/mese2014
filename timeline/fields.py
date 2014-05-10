from django.db import models
import core

class FinancialYearField(models.CharField):

	def __init__(self, *args, **kw_args):
		kw_args['default'] = core.get_timeline()['year']
		kw_args['max_length'] = 4
		kw_args['editable'] = False
		super(FinancialYearField, self).__init__(*args, **kw_args)