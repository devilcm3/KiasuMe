LOCALSETTINGS = True
from settings import *

if  LOCALSETTINGS:
	DEBUG = True
	ALLOWED_HOSTS 	= ['localhost']
	MEDIA_ROOT 		= PROJECT_ROOT + '/media/'
	MEDIA_URL  		= '/media/'
	STATIC_URL 		= '/static/'
	STATICFILES_DIRS = (
	    os.path.join(PROJECT_ROOT,'static/'),
	)
else:
	ALLOWED_HOSTS 	= ['kiasu.me','www.kiasu.me']
	MEDIA_ROOT 		= '/home/devilcm3/webapps/kiasume_cdn/media/'
	MEDIA_URL  		= '/files/media/'
	STATIC_URL 		= '/files/static/'
	# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
	# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'