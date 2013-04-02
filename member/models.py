from django.db import models
from project_dante import settings
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class ProfileManager(UserManager):
	def create_user(self,password=None ,**kwargs):
		if not username:
			raise ValueError('Username is empty')

		user = self.model(**kwargs)
		user.set_password(password)
		user.save(using=self._db)
		return user


class Profile(AbstractUser):
	full_name	= models.CharField(max_length = 200)
	address 	= models.CharField(max_length = 200)
	phone_1 	= models.CharField(max_length = 30)
	phone_2 	= models.CharField(max_length = 30,blank = True)
	fax 		= models.CharField(max_length = 30,blank = True)
	mobile 		= models.CharField(max_length = 30,blank = True)

	def __unicode__(self):
		return self.full_name

	objects		= UserManager()