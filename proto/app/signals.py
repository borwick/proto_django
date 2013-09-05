import logging

from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete


logger = logging.getLogger(__name__)
