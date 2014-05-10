from sae import kvdb
from datetime import datetime
import signals

MIN_TIMELINE = 10800

def init():
	if '_KVClient' not in globals():
		global _KVClient
		_KVClient = kvdb.KVClient(debug = 1)

def get_timeline(create_on_none = True):
	init()
	year = _KVClient.get('year')
	if not year:
		if not create_on_none:
			return None
		else:
			set_timeline(datetime.now().year)
	return {
			'year': year,
			'time_delta': datetime.now()-_KVClient.get('set_time')
	}
	
class TimelineNotExpiredError(Exception):
	pass
	
def set_timeline(year):
	init()
	set_time = _KVClient.get('set_time')
	if set_time and (datetime.now()-set_time).seconds < MIN_TIMELINE:
		raise TimelineNotExpiredError
	_KVClient.set('year', year)
	_KVClient.set('set_time', datetime.now())
	signals.timeline_changed.send(sender = year, year = year)