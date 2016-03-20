"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from deal.models import *
from member.models import *
from datetime import date,time,datetime
import urllib2,urllib
from django.core.files.base import ContentFile

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


	def fb_deal(self):
		source_url = "https://fbcdn-photos-d-a.akamaihd.net/hphotos-ak-ash4/1186104_532294086825592_1426147363_s.png"
		image_content = urllib2.urlopen(source_url)
		image_name = source_url.split('/')[-1]

		deal = Deal()
		deal.date_started = "2013-09-16"
		deal.date_ended = "2013-09-16"
		deal.title = u"FB Test"
		deal.link = "www.google.com"
		deal.content = "This is the test caption"
		deal.promo_image.save(image_name,ContentFile(image_content.read()), save=False)
		deal.member_pk = Profile.objects.get(id=1)
		deal.category_pk = Category.objects.get(id=1)
		deal.save()

