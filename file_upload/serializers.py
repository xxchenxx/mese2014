from rest_framework import serializers
from models import PrivateFile, PublicFile

class FileSerializer(serializers.HyperlinkedModelSerializer):

	file_type = serializers.CharField(write_only = True)
	file_name = serializers.Field(source = 'file.name')
	file_url  = serializers.Field(source = 'file.url')

class PrivateFileSerializer(FileSerializer):

	class Meta:
		model = PrivateFile
		
class PublicFileSerializer(FileSerializer):
	
	class Meta:
		model = PublicFile