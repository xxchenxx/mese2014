from sae import kvdb
from datetime import datetime

def init():
	if '_KVClient' not in globals():
		global _KVClient
		_KVClient = kvdb.KVClient(debug = 1)

def get_timeline():
	init()
	return {
			'year':_KVClient.get('year'),
			'time_delta': datetime.now()-KVClient.get('now')
	}
	
def set_timeline(year):
	init()
	_KVClient.set('year', year)
	_KVClient.set('now', datetime.now())