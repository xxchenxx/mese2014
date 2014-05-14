from django.db import models
import core

class FinancialYearField(models.CharField):

	def __init__(self, *args, **kw_args):
		#self.default = core.get_timeline()['year']
		kw_args['max_length'] = 4
		kw_args['editable'] = False
		super(FinancialYearField, self).__init__(*args, **kw_args)
		
	def pre_save(self, model_instance, add):
		if add:
			value = core.get_timeline()['year']
			setattr(model_instance, self.attname, value)
			print value
			return value
		else:
			return super(FinancialYearField, self).pre_save(model_instance, add)