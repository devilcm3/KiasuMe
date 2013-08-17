from django.db.models.signals import post_save,pre_save,pre_init,post_init
from django.db import models
from django.forms import ModelForm
from member.models import Profile
from datetime import datetime, date
from django.utils import timezone
from uuid import uuid4

import random,os

# Create your models here.
class Category(models.Model):
	name 			= models.CharField(max_length=50)
	priority		= models.IntegerField(max_length=3, blank=True, null=True)

	def __unicode__(self):
		return self.name



class Subcategory(models.Model):
	name 			= models.CharField(max_length=50)
	category_pk 	= models.ForeignKey('Category', related_name='subcategories')
	priority		= models.IntegerField(max_length=3, blank=True, null=True)

	def __unicode__(self):
		return self.name



class Tag(models.Model):
	name 			= models.CharField(max_length=10)

	def __unicode__(self):
		return self.name


class Deal(models.Model):

	def get_file_upload_path(self,*args):
		return "%s/%s/%s%s" %("media/deal", date.today().strftime("%Y/%m/%d"), uuid4(), '.jpeg')

	title			= models.CharField(max_length=150, blank = False)
	slug			= models.SlugField(max_length=200, blank = True)
	link 			= models.URLField(max_length=200, blank = True)
	content 		= models.TextField(blank = False)
	active			= models.BooleanField(default = True)
	date_created	= models.DateTimeField(auto_now_add = True)
	date_modified 	= models.DateTimeField(auto_now = True)
	date_started	= models.DateField()
	date_ended		= models.DateField(blank = True, null = True)
	promo_thumbnail = models.URLField(max_length = 250, blank = True, null = True, default = get_file_upload_path(''))
	promo_image		= models.ImageField(max_length = 250, upload_to = get_file_upload_path, blank = True)
	promo_file		= models.FileField(upload_to = get_file_upload_path, blank = True)
	total_vote		= models.FloatField(default = 0, blank = True)
	member_pk		= models.ForeignKey('member.Profile', blank=True)
	category_pk		= models.ForeignKey('Category')
	subcategory_pk	= models.ForeignKey('Subcategory',blank=True, null=True)
	tag_pk 			= models.ManyToManyField('Tag', blank = True, null = True)

	def __unicode__(self):
		return self.title

	@staticmethod
	def vote(promo_id,vote):
		if vote == '1':
			vote = 1
		elif vote == '-1':
			vote = -1
		Deal.objects.filter(id=promo_id).update(total_vote=models.F('total_vote') + vote)

	def save(self, *args, **kwargs):
		from django.utils.text import slugify
		self.slug = slugify(self.title)

		new = False
		if self.id is None:
			new = True

		if(hasattr(self.promo_image,'file')):
			self.promo_thumbnail = "%s/%s/%s%s" %("media/deal", date.today().strftime("%Y/%m/%d"), uuid4(), '.jpeg')
			super(Deal,self).save(*args, **kwargs)

			from django.core.files.storage import default_storage
			from django.core.files.base import ContentFile
			from PIL import Image, ImageOps
			from cStringIO import StringIO
			img_input = StringIO(self.promo_image.read())
			path 	= str(self.promo_image.file)
			img 	= Image.open(img_input)
			img 	= img.convert("RGB")

			img.thumbnail((1600,1000),Image.ANTIALIAS)
			temp = StringIO()
			img.save(temp,'JPEG',quality=75)

			img.thumbnail((640,480),Image.ANTIALIAS)
			temp2 = StringIO()
			img.save(temp2,'JPEG',quality=75)

			default_storage.delete(path)
			default_storage.save(path,ContentFile(temp.getvalue()))
			default_storage.save(self.promo_thumbnail,ContentFile(temp2.getvalue()))

			temp.close()
			temp2.close()
		else:
			super(Deal,self).save(*args, **kwargs)

		if new:
			from django.contrib.sitemaps import ping_google
			from twitter import *
			from project_dante import settings

			try:
				t = Twitter(auth = OAuth(settings.KIASU_OAUTH_TOKEN, settings.KIASU_OAUTH_SECRET, settings.KIASU_CONSUMER_KEY, settings.KIASU_CONSUMER_SECRET))
				status_msg = self.member_pk.username[:15]+" posted: "+self.title[:80]+"... #discount" +" kiasu.me/dv/"+str(self.id)+" #fb"
				t.statuses.update(status = status_msg)
				ping_google()
			except:
				pass

class DealRating(models.Model):
	vote			= models.NullBooleanField(blank=True,default=None)
	deal_pk			= models.ForeignKey('Deal')
	member_pk		= models.ForeignKey('member.Profile')

class FacebookFeed(models.Model):
	page_name		= models.CharField(max_length=100,blank=True)
	page_id			= models.CharField(max_length=100,blank=True)
	page_link		= models.CharField(max_length=100,blank=True)
	recent_feed		= models.CharField(max_length=100,blank=True)
	category_pk		= models.ForeignKey('Category')
	member_pk		= models.ForeignKey('member.Profile', blank=True, null=True)
	
	def save(self, *args, **kwargs):
		from open_facebook.api import OpenFacebook
		from project_dante import settings

		if not self.member_pk:
			self.member_pk = Profile.objects.get(username="kiasu_bot")
			
		graph = OpenFacebook(settings.FACEBOOK_APP_ID+'|'+settings.FACEBOOK_APP_SECRET)
		data = graph.get(self.page_link)
		self.page_id = data['id']
		self.page_name = data['name']

		super(FacebookFeed,self).save(*args, **kwargs)