import logging

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


logger = logging.getLogger(__name__)


class FIXMEForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

        super(FIXMEForm, self).__init__(*args, **kwargs)
