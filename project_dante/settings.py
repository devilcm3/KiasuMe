# Django settings for project_dante project.
import os,django #,dj_database_url

AWS_ACCESS_KEY_ID = "AKIAJB3JQ6PX7NFMSQQA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "dantecdnsgp"
AWS_QUERYSTRING_AUTH = False
S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
AUTH_USER_MODEL = 'member.Profile'

ADMINS = (('David Tjokroaminoto', 'david.tjokroaminoto@gmail.com'))
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kiasume_db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'kiasu_db_admin',
        'PASSWORD': 'iTcKaKYVs47zXq',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.    
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['kiasu.me','www.kiasu.me']

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Singapore'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT      = '/home/devilcm3/webapps/kiasume_cdn/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL       = '/files/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT     = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL      = '/files/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l=yd^5xg5-$1_g-1_0$dop5!*(0i1%e5&j#6z(ncu@+wj$x&5t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False
}

ROOT_URLCONF = 'project_dante.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project_dante.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT,'templates')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # Uncomment the next line to enable the admin:
    'grappelli',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'social_auth',
    'member',
    'deal',
    'store',
    'django_cleanup',
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_APP_ID = '139156246267349'
FACEBOOK_API_SECRET = '9fae1ebd0fb9912bf9b1e9d47c735795'
TWITTER_CONSUMER_KEY = 'i4yaIqzsHJLLufcYXnzFQ'
TWITTER_CONSUMER_SECRET = 'IIHqHtRp61PJEZiJGLuLzaLRunmURKM1g0DjTBIgeA'

KIASU_CONSUMER_KEY = '4TSdAbMvYknaSJ1Vhse9w'
KIASU_CONSUMER_SECRET = 'oX4Uhow9Ow4x2bkpifQdLg4lTkJJRDGMsmeCJg3uFQ'
KIASU_OAUTH_TOKEN = '1379317524-I31uMphW3yDJ1dLtSRYAzdlprkBd1dIan6M0OAG'
KIASU_OAUTH_SECRET = 'mdonJv5oU50Q4SoIuyV1PApIiOdXLwfuyk7hawHILTU'
TWITTER_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

SOCIAL_AUTH_BACKEND_ERROR_URL = '/login-error/'
SOCIAL_AUTH_USER_MODEL = 'member.Profile'
SOCIAL_AUTH_DEFAULT_USERNAME = 'social_profile'


SOUTH_MIGRATION_MODULES = {
    'member':'ignore',
    'social_auth':'ignore',
}
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'SMTP.WEBFACTION.COM'
EMAIL_HOST_USER = 'kiasu_noreply'
EMAIL_HOST_PASSWORD = 'WaaQFU28YfgVYa'

try:
    from local_settings import *
except ImportError, e:
    pass