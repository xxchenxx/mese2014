from accounts.models import Bank
import cron

class ShareProfitsCron(cron.Cron):

	def do(self):
		for bank in Bank.objects.all():
			bank.share_profits()