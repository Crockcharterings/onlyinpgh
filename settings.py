# Django settings for onlyinpgh project.

import os, datetime
# import settings that differ based on deployment
import settings_local

def to_abspath(path):
    '''prepends ROOT_DIR setting from settings_local to the given path'''
    return os.path.join(settings_local.ROOT_DIR, path)

DEBUG = settings_local.DEBUG
TEMPLATE_DEBUG = settings_local.TEMPLATE_DEBUG

ADMINS = settings_local.ADMINS
MANAGERS = settings_local.ADMINS

DATABASES = {
    'default': settings_local.DB_DEFAULT
}
DATABASES['default']['TEST_CHARSET'] = 'utf8'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = settings_local.TIME_ZONE

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = settings_local.MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = settings_local.STATIC_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (    
    to_abspath('boilerplate'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bqv*s&^)0l8*xe(i2u!oyr9s&5y^k-$o^8x9zo69b3%-sixer)'

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
)

ROOT_URLCONF = 'onlyinpgh.urls'

TEMPLATE_DIRS = (
    to_abspath('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'django_extensions',
    'onlyinpgh.places',
    'onlyinpgh.events',
    'onlyinpgh.identity',
    'onlyinpgh.news',
    'onlyinpgh.chatter',
    'onlyinpgh.tagging',
    'onlyinpgh.offers',
    'onlyinpgh.checkin',
    'onlyinpgh.outsourcing',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
_timestamp = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S.%f')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': to_abspath('logs/debug.log')
        },
        'resolve_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': to_abspath('logs/resolve.log')
        },
        'outsourcing_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': to_abspath('logs/outsourcing.log')
        },
        'fb_import_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple_timestamped',
            'filename': to_abspath('logs/imports/facebook_%s.log' % _timestamp),
            'delay': True,      # only open if message is emitted
            'mode': 'w'
        },
        'ical_import_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple_timestamped',
            'filename': to_abspath('logs/imports/ical_%s.log' % _timestamp),
            'delay': True,      # only open if message is emitted
            'mode': 'w'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'onlyinpgh.debugging': {
            'handlers': ['console','debug_file'],
            'level':'DEBUG',
            'propagate': False
        },
        'onlyinpgh.resolve': {
            'handlers': ['console','resolve_file'],
            'level':'DEBUG',
            'propagate': False
        },
        'onlyinpgh.outsourcing': {
            'handlers': ['console','outsourcing_file'],
            'level':'DEBUG',
            'propagate': False
        },
        'onlyinpgh.fb_import': {
            'handlers': ['console','fb_import_file'],
            'level':'DEBUG',
            'propagrate': False
        },
        'onlyinpgh.ical_import': {
            'handlers': ['console','ical_import_file'],
            'level':'DEBUG',
            'propagrate': False
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'simple_timestamped': {
            'format': '%(levelname)s %(asctime)s %(message)s'  
        },
    }
}

FIXTURE_DIRS = ( to_abspath('fixtures'),
)