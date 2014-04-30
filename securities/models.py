from django.db import models

class Fond(models.Model):

	display_name = models.CharField(unique = True, max_length = 20)
	
	@property
	def code_name(self):
		return '%.6d' % self.id
		
	class Meta:
		ordering = ['display_name']
		abstract = True