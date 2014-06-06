from rest_framework.relations import PrimaryKeyRelatedField
from files.serializers import FileField

class WritableRelatedField(PrimaryKeyRelatedField):

	def __init__(self, *args, **kwargs):
		self.serializer_class = kwargs.pop('serializer_class', None)
		super(WritableRelatedField, self).__init__(*args, **kwargs)
		
	def field_to_native(self, obj, field_name):
		return self.serializer_class(getattr(obj, field_name)).data