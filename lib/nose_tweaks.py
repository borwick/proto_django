"""
When added to the NOSE_PLUGINS list, this simple plugin will make
south be less chatty when running nose tests. Credit goes to

http://pypede.wordpress.com/2012/06/17/disable-south-debug-logging-when-testing-apps-with-nose-in-django/
"""
import logging

from nose.plugins import Plugin


class SilenceSouth(Plugin):
    south_logging_level = logging.ERROR

    def configure(self, options, conf):
        super(SilenceSouth, self).configure(options, conf)
        logging.getLogger('south').setLevel(self.south_logging_level)
