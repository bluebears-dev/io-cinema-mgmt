import json
import os

from django.forms.widgets import Input

from app.settings import BASE_DIR


class LayoutWidget(Input):
    """
    Base class for all <input> widgets.
    """
    input_type = 'checkbox'
    template_name = os.path.join(BASE_DIR, 'cinema', 'templates', 'widgets', 'layout_widget.html')

    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.format = format or None

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['type'] = self.input_type
        return context

    def format_value(self, value):
        if value is None:
            return json.dumps(value)
        return json.dumps(value[0])

    def value_from_datadict(self, data, files, name):
        return data.getlist(name), data.get('rows'), data.get('cols')
