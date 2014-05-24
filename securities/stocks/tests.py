"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *
from django.contrib.auth.models import User
from accounts.models import *

class StockTest(TestCase):
		# # def test_basic_addition(self):
				# """
				# Tests that 1 + 1 always equals 2.
				# """
				# self.assertEqual(1 + 1, 2)

	def setUp(self):
		self.user1 = Person.objects.get(display_name = 'test')
		self.user2 = Person.objects.get(display_name = 'test2')
		self.company = User.objects.create_user(username = 'cpy', password = 'cpy').profile.create_info(class_name = 'Company')
		self.stock = Stock.objects.create(display_name = 'STK', publisher = Company.objects.get(pk=1), current_price = '1.0')
		
	def test_application(self):
		self.Share.objects.create(owner = self.user1, stock = self.stock, shares = 10000)
		self.stock.apply(self.user1, 0.9, 'sell', 10)
		
user1, user2 = Person.objects.all()
stk = Stock.objects.get(pk=1)
stk.apply(user1, 0.9, 'sell', 1000)
stk.apply(user2, 0.9, 'buy', 1000)

from django.db import connection
print len(connection.queries)