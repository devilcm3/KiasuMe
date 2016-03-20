from django.db import models
from project_dante import settings
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import date, timedelta
from member.utils import *
# Create your models here.

class Profile(AbstractUser):
	middle_name	= models.CharField(max_length = 100, blank = True)
	address 	= models.CharField(max_length = 200,blank = True)
	landline_1 	= models.CharField(max_length = 30,blank = True)
	landline_2 	= models.CharField(max_length = 30,blank = True)
	fax 		= models.CharField(max_length = 30,blank = True)
	mobile 		= models.CharField(max_length = 30,blank = True)
	website		= models.URLField(blank = True)
	deal_rating_pk		= models.ManyToManyField('deal.Deal', through = 'deal.DealRating', null = True, blank = True)
	store_rating_pk		= models.ManyToManyField('store.Store', through = 'store.StoreRating', null = True, blank = True)

	objects		= UserManager()

	def __unicode__(self):
		return self.username

	def save(self, *args, **kwargs):
		super(Profile,self).save(*args, **kwargs)

class RegEmail(models.Model):
	email 			= models.EmailField()
	verification	= models.CharField(max_length = 150)
	date_expired	= models.DateField(default = (date.today() + timedelta(days=7) ))
	profile_pk		= models.ForeignKey('Profile')

	def save(self, *args, **kwargs):
		import uuid
		self.email = self.profile_pk.email
		self.verification = str(uuid.uuid4())
		super(RegEmail,self).save(*args, **kwargs)

		member_confirm_mail(mid = self.id,email = self.email,username = self.profile_pk.username,verification = self.verification)

		