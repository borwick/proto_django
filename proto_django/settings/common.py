DEBUG = False
TEMPLATE_DEBUG = DEBUG

# DEFINE DATABASES IN local_settings.py

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# 
# FIXME:
STATIC_ROOT = '/path/to/static/root/'


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'proto_django.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'proto_django.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT_DIR, 'templates'),
)

INSTALLED_APPS = apps_from('app') + (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:

    'django.contrib.admindocs',
    'django.contrib.humanize',
    'djcelery',
    'djsupervisor',
    'social.apps.django_app.default',
    # FIXME incompatability with Django 1.7 b/c uses models before
    # setup:
    # 
    # 'registration',
    'passwords',
    'crispy_forms',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
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
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
# project's top-level directories:
        'app': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
            },
        'lib': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
            },
    }
}

import djcelery
djcelery.setup_loader()
CELERY_TASK_SERALIZER = "json"
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    )

# --- Social Auth:
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend',
    # 'social_auth.backends.yahoo.YahooBackend',
    # 'social_auth.backends.browserid.BrowserIDBackend',
    # FIXME get LinkedIn backend to work (returns 401 unauthorized)
    # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    # 'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    # 'social_auth.backends.contrib.orkut.OrkutBackend',
    # 'social_auth.backends.contrib.foursquare.FoursquareBackend',
    # 'social_auth.backends.contrib.github.GithubBackend',
    # 'social_auth.backends.contrib.vk.VKOAuth2Backend',
    # 'social_auth.backends.contrib.live.LiveBackend',
    # 'social_auth.backends.contrib.skyrock.SkyrockBackend',
    # 'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    # 'social_auth.backends.contrib.readability.ReadabilityBackend',
    # 'social_auth.backends.contrib.fedora.FedoraBackend',
    # 'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
    )


TWITTER_CONSUMER_KEY         = 'FIXME'
TWITTER_CONSUMER_SECRET      = 'FIXME'
FACEBOOK_APP_ID              = 'FIXME'
FACEBOOK_API_SECRET          = 'FIXME'
# LINKEDIN_CONSUMER_KEY        = ''
# LINKEDIN_CONSUMER_SECRET     = ''
# ORKUT_CONSUMER_KEY           = ''
# ORKUT_CONSUMER_SECRET        = ''
# GOOGLE_CONSUMER_KEY          = ''
# GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = 'FIXME'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'FIXME'
# FOURSQUARE_CONSUMER_KEY      = ''
# FOURSQUARE_CONSUMER_SECRET   = ''
# VK_APP_ID                    = ''
# VK_API_SECRET                = ''
# LIVE_CLIENT_ID               = ''
# LIVE_CLIENT_SECRET           = ''
# SKYROCK_CONSUMER_KEY         = ''
# SKYROCK_CONSUMER_SECRET      = ''
# YAHOO_CONSUMER_KEY           = ''
# YAHOO_CONSUMER_SECRET        = ''
# READABILITY_CONSUMER_SECRET  = ''
# READABILITY_CONSUMER_SECRET  = ''
DISQUS_CLIENT_ID = 'FIXME'
DISQUS_CLIENT_SECRET = 'FIXME'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

# LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress']
# # Field selectors determine what data social_auth will get from linkedin
# LINKEDIN_EXTRA_FIELD_SELECTORS = [
#     'email-address',
# ]
# # extra_data determines what data will be stored in a JSON field in the
# # UserSocialAuth table. This should parallel the field selectors.
# LINKEDIN_EXTRA_DATA = [('id', 'id'),
#                        ('first-name', 'first_name'),
#                        ('last-name', 'last_name'),] + [
#                            (field, field.replace('-', '_'), True)
#                            for field in LINKEDIN_EXTRA_FIELD_SELECTORS
#                        ]

DISQUS_AUTH_EXTRA_ARGUMENTS = {'scope': 'read,email'}

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    #'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    # This prevents social_auth from creating accounts:
    # 'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'
)

# Django-registration settings:
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window


LOGIN_REDIRECT_URL = '/profile/'

# django-passwords:
PASSWORD_MIN_LENGTH = 8
PASSWORD_COMPLEXITY = { "UPPER":  1, "LOWER":  1, "DIGITS": 1 }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(PROJECT_ROOT_DIR, 'var/cache'),
    }
}
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

CRISPY_TEMPLATE_PACK = 'uni_form'
