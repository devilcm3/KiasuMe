from django.db import models
from datetime import datetime

# Create your models here.
class Province(models.Model):
	name 		= models.CharField(max_length=50)

	def __unicode__(self):
		return self.name



class Area(models.Model):
	name 		= models.CharField(max_length=100)
	province_pk = models.ForeignKey('Province')

	def __unicode__(self):
		return self.name



class Store(models.Model):
	name 		= models.CharField(max_length=200)
	address 	= models.CharField(max_length=200)
	postcode	= models.IntegerField(max_length=10)
	phone_1		= models.CharField(max_length=30, blank = True)
	phone_2		= models.CharField(max_length=30, blank = True)
	fax 		= models.CharField(max_length=30, blank = True)
	image		= models.ImageField(upload_to="media/store", blank=True)
	total_vote	= models.FloatField(default = 0)
	member_pk	= models.ForeignKey('member.Profile')
	province_pk	= models.ForeignKey('Province')
	area_pk		= models.ForeignKey('Area')	

	def __unicode__(self):
		return self.name



class StoreRating(models.Model):
	vote		= models.NullBooleanField(blank=True, default=None)
	store_pk	= models.ForeignKey('Store')
	member_pk	= models.ForeignKey('member.Profile')

	def __unicode__(self):
		return self.vote