import sys
import os.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'mese2014.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'mese2014'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'common'))

import sae
from mese2014 import wsgi
application = sae.create_wsgi_app(wsgi.application)
try:
	import pylibmc
	sys.modules['memcache'] = pylibmc
except ImportError:
	pass
	
from lib import rest_framework
sys.modules['rest_framework'] = rest_framework