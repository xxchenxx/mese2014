from django.core.urlresolvers import reverse
from rest_framework import serializers, pagination
import models
from django.contrib.auth.models import User
import accounts.serializers

class PassageSerializer(serializers.ModelSerializer):

	author = accounts.serializers.UserSerializer()
	
	class Meta:
		model = models.Passage
		#fields = ['content', 'title', 'author', 'created_time']
		
class CommentSerializer(serializers.ModelSerializer):
	
	author = accounts.serializers.UserSerializer()
	
	class Meta:
		model = models.Comment
		exclude = ['passage']
		
class PaginatedCommentSerializer(pagination.PaginationSerializer):
	class Meta:
		object_serializer_class = CommentSerializer