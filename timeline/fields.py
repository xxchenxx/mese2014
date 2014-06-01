from django.db import models
from core import Timeline

class FinancialYearField(models.CharField):

	def __init__(self, *args, **kw_args):
		kw_args['max_length'] = 5
		kw_args['editable'] = False
		super(FinancialYearField, self).__init__(*args, **kw_args)
		
	def pre_save(self, model_instance, add):
		if add:
			data = Timeline().get()
			value = '%(year)d%(quarter)d' % data
			setattr(model_instance, self.attname, value)
			return value
		else:
			return super(FinancialYearField, self).pre_save(model_instance, add)