from django.db import connection

class SQLMiddleware(object):

	def process_response(self, request, response):
		print "SQL: %d" % len(connection.queries)
		return response