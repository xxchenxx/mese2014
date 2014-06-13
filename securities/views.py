from annoying.decorators import render_to
from django.http import Http404
from .funds.models import Fund
from .stocks.models import Stock
from .bonds.models import Bond
from django.shortcuts import get_object_or_404

@render_to('securities/index.html')
def index(request):
	return {}

_CLASSES = {
	'fund': Fund,
	'stock': Stock,
	'bond': Bond
}
	
@render_to('securities/detail.html')
def detail(request):
	fund_type = request.REQUEST.get('type','').lower()
	id = request.REQUEST.get('id','').lower()
	if fund_type not in _CLASSES:
		raise Http404
	try:
		id = int(id)
	except ValueError:
		raise Http404
		
	obj = get_object_or_404(_CLASSES[fund_type], id = id)
	return {'type': fund_type, 'object': obj}