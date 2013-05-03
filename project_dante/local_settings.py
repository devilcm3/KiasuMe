from settings import *
LOCALSETTINGS = True
DEBUG = True

if  LOCALSETTINGS:
	DATABASES = {
	    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'project_dante',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'davidcokro_12',
        'PASSWORD': '',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
        }
    }
	ALLOWED_HOSTS 	= ['localhost']
	MEDIA_ROOT 		= PROJECT_ROOT + '/media/'
	MEDIA_URL  		= '/media/'
	STATIC_URL 		= '/static/'
	STATICFILES_DIRS = (
	    os.path.join(PROJECT_ROOT,'static/'),
	)
else:
	pass
	# AMAZON S3 STORAGE
	# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
	# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'