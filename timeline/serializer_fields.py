#encoding=utf8
from rest_framework.fields import WritableField

class FinancialYearField(WritableField):
	
	def __init__(self, *args, **kwargs):
		super(FinancialYearField,self).__init__(*args,**kwargs)
		self.read_only=True
		self.required=False
	
	def to_native(self, value):
		return '%s-%s' % (value[:-1],value[-1:])