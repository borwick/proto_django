import logging

from dajaxice.decorators import dajaxice_register

from lib.json_shortcuts import to_json


logger = logging.getLogger(__name__)

@dajaxice_register(method='GET', name='FIXME')
def FIXME(request):
    return to_json('')
