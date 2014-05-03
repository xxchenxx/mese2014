from django.core.urlresolvers import reverse
from djangorestframework.views import View
from djangorestframework.resources import ModelResource
import models

class PassageResource(ModelResource):

	model = models.Passage
	fields = ['content', 'title',]# 'author']