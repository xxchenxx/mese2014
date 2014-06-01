from cron import Cron
from models import Fund

class ShareProfitsCron(Cron):
	
	def do(self):
		for fund in Fund.objects.published():
			fund.share_profits()
			
class CheckPublishCron(Cron):
	
	def get_interval_minutes(self):
		return 5
	
	def do(self):
		for fund in Fund.objects.filter(published_time__lte = self.now, published = False):
			fund.publish()