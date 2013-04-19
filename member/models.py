from django.db import models
from project_dante import settings
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class Profile(AbstractUser):
	middle_name	= models.CharField(max_length = 100, blank = True)
	address 	= models.CharField(max_length = 200)
	phone_1 	= models.CharField(max_length = 30)
	phone_2 	= models.CharField(max_length = 30,blank = True)
	fax 		= models.CharField(max_length = 30,blank = True)
	mobile 		= models.CharField(max_length = 30,blank = True)
	promotion_rating_pk		= models.ManyToManyField('promotion.Promotion', through = 'promotion.PromotionRating')
	store_rating_pk			= models.ManyToManyField('store.Store', through = 'store.StoreRating')

	objects		= UserManager()

	def __unicode__(self):
		return self.first_name
