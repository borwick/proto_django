"""
Settings needed in all environments besides prod.
"""

INSTALLED_APPS += (
    'django_nose',
    )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_PLUGINS = [
    'lib.nose_tweaks.SilenceSouth',
]
