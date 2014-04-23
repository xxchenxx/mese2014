import sys
import os.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'mese2014.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'mese2014'))

import sae
from mese2014 import wsgi
application = sae.create_wsgi_app(wsgi.application)
#import pylibmc
#sys.modules['memcache'] = pylibmc