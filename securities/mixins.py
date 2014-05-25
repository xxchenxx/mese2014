from futures.mixins import *
from bonds.mixins import *
from funds.mixins import *
from stocks.mixins import *

class HasStockBondMixin(HasStockMixin, HasBondMixin):
	
	class Meta:
		abstract = True
		
__all__ = filter(lambda x: x.endswith('Mixin'), globals().iterkeys())