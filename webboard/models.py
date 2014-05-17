from django.db import models
from django.contrib.auth.models import User
from common.fields import FinancialYearField
class Passage(models.Model):
	
	CONFERENCE = 'CO'
	MEDIA = 'MED'
	GOVERNMENT = 'GOV'
	COMPANY = 'COM'
	
	TYPE_CHOICES = (
			(CONFERENCE, 'conference'),
			(MEDIA, 'media'),
			(GOVERNMENT, 'government'),
			(COMPANY, 'company'),
	)
	
	type = models.CharField(max_length = 3, choices = TYPE_CHOICES)
	title = models.CharField(max_length = 255, unique = True)
	created_time = models.DateTimeField(auto_now_add = True)
	year = FinancialYearField()
	author = models.ForeignKey(User, related_name = 'passages')
	content = models.TextField()
	
	def __unicode__(self):
		return "Passage: %s" % self.title
		
	class Meta:
		ordering = ['-created_time', 'title']
		
class Comment(models.Model):
	
	content = models.TextField()
	author = models.ForeignKey(User, related_name = 'comments')
	created_time = models.DateTimeField(auto_now_add = True)
	passage = models.ForeignKey(Passage, related_name = 'comments')
	respond_comment = models.ForeignKey('self', related_name = 'responses', blank = True, null = True)
	
	def __unicode__(self):
		return "%s comment for passage %s" % (self.author.username, self.passage.title)
		
	class Meta:
		ordering = ['-created_time']