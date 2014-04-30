from sae import kvdb
from datetime import datetime

MIN_TIMELINE = 10800

def init():
	if '_KVClient' not in globals():
		global _KVClient
		_KVClient = kvdb.KVClient(debug = 1)

def get_timeline():
	init()
	year = _KVClient.get('year')
	if not year:
		return None
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