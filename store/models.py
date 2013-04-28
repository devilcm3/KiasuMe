from django.db import models
from datetime import datetime

# Create your models here.
class Area(models.Model):
	name 		= models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class Store(models.Model):
	def store_thumbnail(self,*args,**kwargs):
		return "media/store/%s" %(self.id)

	name 		= models.CharField(max_length=200)
	address 	= models.CharField(max_length=200)
	postcode	= models.IntegerField(max_length=10)
	landline_1	= models.CharField(max_length=30, blank = True)
	landline_2	= models.CharField(max_length=30, blank = True)
	mobile		= models.CharField(max_length=30, blank = True)
	fax 		= models.CharField(max_length=30, blank = True)
	email 		= models.EmailField(blank = True)
	website		= models.URLField(blank = True)
	image		= models.ImageField(upload_to=store_thumbnail, blank=True)
	total_vote	= models.FloatField(default = 0)
	member_pk	= models.ForeignKey('member.Profile')
	area_pk		= models.ForeignKey('Area')

	def __unicode__(self):
		return self.name


class StoreRating(models.Model):
	vote		= models.NullBooleanField(blank=True, default=None)
	store_pk	= models.ForeignKey('Store')
	member_pk	= models.ForeignKey('member.Profile')

	def __unicode__(self):
		return self.vote