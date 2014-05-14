from django.db import connection
from models import get_fond_class
import consts

def update_fonds(fond_class, data):
	cursor = connection.cursor()
	for fond_type in consts.fond_types:
		cls = get_fond_class(fond_type)
		cursor.execute("""UPDATE %s SET %s = CASE id %s END WHERE id IN %s""", [
				cls._meta.db_table,
				cls.current_price_field,
				' '.join(('WHEN %s THEN %s' % (str(i),j) for i,j in data.iteritems())),
				','.join(data.iterkeys()),
		])