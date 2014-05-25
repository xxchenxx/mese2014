from common.mixins import *
from models import Share, Application
from signals import application_updated

__all__ = ['HasStockMixin']

class HasStockMixin(HasAssetsMixin):

	stock_shares = generic.GenericRelation(
			'stocks.Share',
			content_type_field = 'owner_type',
			object_id_field = 'owner_object_id'
	)
	
	def get_share(self, stock, create = False, **kwargs):
		try:
			return self.stock_shares.get(stock = stock)
		except Share.DoesNotExist:
			if create:
				return Share(owner = self, stock = stock, **kwargs)
				
	def __apply(self, command, stock, price, shares):
		application = Application(stock = stock, applicant = self, price = price, command = command, shares = shares)
		application.clean()
		application.save()
		application_updated.send(self, application = application)
		
		return application
		
	def buy(self, stock, price, shares):
		self.__apply(Application.BUY, stock, price, shares)
		
	def sell(self, stock, price, shares):
		self.__apply(Application.SELL, stock, price, shares)
	
	class Meta:
		abstract = True