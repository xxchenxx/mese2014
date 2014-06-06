from django.forms import ModelForm
import models

class PassageForm(ModelForm):

	class Meta:
		model = models.Passage
		exclude = ['created_time']

class CommentForm(ModelForm):
	
	class Meta:
		model = models.Comment
		exclude = ['created_time']