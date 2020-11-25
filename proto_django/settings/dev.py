# (can be overridden by local_settings.py)
DEBUG = True

# in case we turn DEBUG off for testing:
ALLOWED_HOSTS = '*'

ADMINS = (
    ('FIXME', 'fixme@example.com'),
)

MANAGERS = ADMINS

# DEFINE DATABASES IN local_settings.py

SITE_ID = 1

INSTALLED_APPS += (
    'django_extensions',
)

MIDDLEWARE += (
)

# for debug toolbar:
INTERNAL_IPS = ('127.0.0.1',)

# reset logging to DEBUG:
for top_level_dirs in ('app', 'lib'):
    LOGGING['loggers'][top_level_dirs]['level'] = 'DEBUG'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
   }
    }
