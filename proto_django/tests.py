from django.test import TestCase
from django.conf import settings


class SettingsVariablesTest(TestCase):
    SETTINGS_VARIABLES = ('DATABASES',
                          'SECRET_KEY',
                          'STATIC_ROOT',
                          'EMAIL_HOST',
                          'EMAIL_PORT',
                          'EMAIL_HOST_USER',
                          'EMAIL_HOST_PASSWORD',
                          'EMAIL_USE_TLS',
                          'BROKER_URL',
                          'CELERY_RESULT_BACKEND',
                          'CELERYD_CONCURRENCY',
                          'CELERYD_NODES',
                          'CELERY_RESULT_BACKEND',
                          'ALLOWED_HOSTS',
                          )

    def testVariableExists(self):
        """
        Test particularly for variables that must be in
        local_settings.py
        """
        for var in self.SETTINGS_VARIABLES:
            self.assertTrue(hasattr(settings, var),
                            msg="Test if %s is in settings" % var)
