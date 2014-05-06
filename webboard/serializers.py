from django.core.urlresolvers import reverse
from rest_framework import serializers
import models
from django.contrib.auth.models import User
import accounts.serializers

class PassageSerializer(serializers.ModelSerializer):

	author = accounts.serializers.UserSerializer()
	
	class Meta:
		model = models.Passage
		#fields = ['content', 'title', 'author', 'created_time']