from django.db.models.signals import post_save,pre_save,pre_init,post_init
from django.db import models
from django.forms import ModelForm
from member.models import Profile
from datetime import datetime, date
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
	category_pk 	= models.ForeignKey('Category')
	priority		= models.IntegerField(max_length=3, blank=True, null=True)

	def __unicode__(self):
		return self.name



class Tag(models.Model):
	name 			= models.CharField(max_length=10)

	def __unicode__(self):
		return self.name


class Promotion(models.Model):

	def get_file_upload_path(self,*args):
		return "%s/%s/%s%s" %("media/promotion", date.today().strftime("%Y/%m/%d"), uuid4(), '.jpeg')

	title			= models.CharField(max_length=200, blank = False)
	content 		= models.TextField(blank = False)
	active			= models.BooleanField(default = True)
	date_created	= models.DateTimeField(auto_now_add = True)
	date_modified 	= models.DateTimeField(auto_now = True)
	date_started	= models.DateField(default = datetime.now())
	date_ended		= models.DateField(default = datetime.now())
	promo_thumbnail = models.SlugField(max_length = 250, blank = True, null = True, default = get_file_upload_path(''))
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
		Promotion.objects.filter(id=promo_id).update(total_vote=models.F('total_vote') + vote)

	def save(self, *args, **kwargs):
		if(hasattr(self.promo_image,'file')):
			self.promo_thumbnail = "%s/%s/%s%s" %("media/promotion", date.today().strftime("%Y/%m/%d"), uuid4(), '.jpeg')

			super(Promotion,self).save(*args, **kwargs)

			from django.core.files.storage import default_storage
			from django.core.files.base import ContentFile
			from PIL import Image, ImageOps
			from cStringIO import StringIO
			img_input = StringIO(self.promo_image.read())
			path 	= str(self.promo_image.file)
			img 	= Image.open(img_input)
			img 	= img.convert("RGB")

			img.thumbnail((1000,1000),Image.ANTIALIAS)
			temp = StringIO()
			img.save(temp,'JPEG',quality=75)

			img.thumbnail((320,240),Image.ANTIALIAS)
			temp2 = StringIO()
			img.save(temp2,'JPEG',quality=75)

			default_storage.save(path,ContentFile(temp.getvalue()))
			default_storage.save(self.promo_thumbnail,ContentFile(temp2.getvalue()))

			temp.close()
			temp2.close()
		else:
			super(Promotion,self).save(*args, **kwargs)

class PromotionRating(models.Model):
	vote			= models.NullBooleanField(blank=True,default=None)
	promotion_pk	= models.ForeignKey('Promotion')
	member_pk		= models.ForeignKey('member.Profile')