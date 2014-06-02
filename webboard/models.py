from django.db import models
from django.contrib.auth.models import User
from common.fields import FinancialYearField
from common.utils import check_base_class_by_name
from files.models import PublicFile

class Passage(models.Model):
	
	GOVERNMENT = 'GOV'
	MEDIA = 'MED'
	ENTERPRISE = 'ENT'
	FUND = 'FUN'
	CONFERENCE = 'CON'
	
	TYPE_MAP = {
		'Government': GOVERNMENT,
		'Media': MEDIA,
		'Enterprise': ENTERPRISE,
		'Fund': FUND
	}
	TYPE_CHOICES = map(lambda x:(x[1], x[0]), TYPE_MAP.iteritems())
	
	type = models.CharField(max_length = 3, editable = False, choices = TYPE_CHOICES)
	title = models.CharField(max_length = 255)
	created_time = models.DateTimeField(auto_now_add = True)
	year = FinancialYearField()
	author = models.ForeignKey(User, related_name = 'passages')
	content = models.TextField()
	attachments = models.ManyToManyField(PublicFile, related_name = 'passages')
	
	def clean_fields(self, *args, **kwargs):
		if not self.type and self.author:
			res = filter(lambda x:check_base_class_by_name(self.author.profile.info, x), self.TYPE_MAP.iterkeys())
			assert res
			self.type = self.TYPE_MAP[res[0]]
			
		super(Passage, self).clean_fields(*args, **kwargs)
	
	def __unicode__(self):
		return "Passage: %s" % self.title
		
	class Meta:
		ordering = ['-created_time', 'title']
		
class Comment(models.Model):
	
	content = models.TextField()
	author = models.ForeignKey(User, related_name = 'comments')
	created_time = models.DateTimeField(auto_now_add = True)
	passage = models.ForeignKey(Passage, related_name = 'comments')
	#respond_comment = models.ForeignKey('self', related_name = 'responses', blank = True, null = True)
	
	def __unicode__(self):
		return "%s comment for passage %s" % (self.author.username, self.passage.title)
		
	class Meta:
		ordering = ['-created_time']