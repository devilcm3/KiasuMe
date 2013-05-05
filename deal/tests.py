"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from deal.models import *
from datetime import date,time,datetime

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class DealTest(TestCase):
	def deal_range(self):
		for i in xrange(1,10000):
			today = [
				datetime.combine(date.today(),time.min),
				datetime.combine(date.today(),time.max)
			]
			Deal.objects.filter(date_created__range=(today[0],today[1])).filter(active=True, total_vote__gt = 0).only('id','title').order_by('-total_vote')[:5]

	def deal_gt(self):
		for i in xrange(1,10000):
			Deal.objects.filter(date_created__gt=date.today()).filter(active=True, total_vote__gt = 0).only('id','title').order_by('-total_vote')[:5]

