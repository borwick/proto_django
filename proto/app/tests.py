from django.test import TestCase

import factory

from .models import FIXME


#---- Factories
class FIXMEFactory(factory.DjangoModelFactory):
    FACTORY_FOR = FIXME


#---- Tests
