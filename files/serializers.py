from rest_framework import serializers
from models import PrivateFile, PublicFile,	File
import os.path

class FileField(serializers.FileField):

	encode_file = lambda self, obj:{
			"file_name": os.path.basename(obj.file.name),
			"file_url":obj.file.url,
			"id": obj.id,
	}

	def	__init__(self, *args, **kwargs):
		self.type = kwargs.pop('type', 'private')
		assert self.type in ('public','private')
		self.many = kwargs.pop('many', False)
		super(FileField, self).__init__(*args, **kwargs) 
		
	def from_native(self, value):
		cls = self.type == 'private' and PrivateFile or PublicFile
		if self.many:
			assert isinstance(value, (tuple, list))
			return cls.objects.filter(pk__in =	value)
		else:
			assert isinstance(value, (str, int))
			return cls.objects.get(pk = value)
		
	def to_native(self, value):
		if self.many:
			return [self.encode_file(file) for file in value.all()]
		else:
			if value is None:
				return
			return self.encode_file(value)

class FileSerializer(serializers.ModelSerializer):

	file_type = serializers.CharField(write_only = True)
	name = serializers.SerializerMethodField('get_file')
	file = serializers.FileField(write_only = True)
	url  = serializers.Field(source = 'file.url')
	
	def get_file(self, obj):
		return os.path.basename(obj.file.name)

class PrivateFileSerializer(FileSerializer):

	class Meta:
		model = PrivateFile
		
class PublicFileSerializer(FileSerializer):
	
	class Meta:
		model = PublicFile