import json
import os

from django.forms.widgets import Input

from app.settings import BASE_DIR


class LayoutWidget(Input):
    """
        Layout widget class.
        It dynamically creates layout form based on form values of rows and cols.
    """
    input_type = 'checkbox'
    template_name = os.path.join(BASE_DIR, 'cinema', 'templates', 'widgets', 'layout_widget.html')

    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.format = format or None

    def get_context(self, name, value, attrs):
        """
            Sets context with keys like type of value to template
        """
        context = super().get_context(name, value, attrs)
        context['widget']['type'] = self.input_type
        return context

    def format_value(self, value):
        """
            Return value to template.
            Checks if its value after failed validation of from model.
        """
        if len(value) and isinstance(value[0], list):
            return value[0]
        return value

    def value_from_datadict(self, data, files, name):
        """
            Return tuple from widget template: layout as list, rows and cols.
        """
        return data.getlist(name), data.get('rows'), data.get('cols')
