from django.core.urlresolvers import reverse
from rest_framework import serializers
import models
from django.contrib.auth.models import User

class PassageSerializer(serializers.ModelSerializer):

	author = serializers.RelatedField(read_only = True, source = 'author.profile.info.display_name')
	
	class Meta:
		model = models.Passage
		fields = ['content', 'title', 'author', 'created_time']
		
# class UserSerializer(serializers.ModelSerializer):
	
	# class Meta:
		# model = User
		# fields = ['username', 'pk']