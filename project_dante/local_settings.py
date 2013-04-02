LOCALSETTINGS = False
from settings import *

if  LOCALSETTINGS:
	DEBUG = True
	ALLOWED_HOSTS = ['localhost']
	STATIC_URL = '/static/'
	STATICFILES_DIRS = (
	    '', os.path.join(PROJECT_ROOT,'static/')
	)