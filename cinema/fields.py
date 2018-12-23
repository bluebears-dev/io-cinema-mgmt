import re

from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import Field, NumberInput
from django.utils import formats
from django.utils.translation import gettext as _

from cinema.widgets import LayoutWidget


def get_row_label(row_index):
    row_symbols = "ABCDEFGHIJKLMNOPQRSTUWVXYZ"
    label = []
    number = row_index - 1

    if number == 0:
        label.append(0)
    else:
        while number > 0:
            modulo = number % len(row_symbols)
            number = (number - modulo) // len(row_symbols)
            label.append(modulo)
        if len(label) > 1:
            label[-1] -= 1

    return ''.join(map(lambda v: row_symbols[v], reversed(label)))


def get_col_label(col_index):
    return str(col_index)


class LayoutField(Field):
    rows = 0
    cols = 0
    widget = LayoutWidget

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self, value):
        """
            Check if list contains only numbers and is not none.
        """
        if len(value) == 0:
            raise ValidationError(_('Sala musi posiadać siedzenia'))
        try:
            for num in value:
                index = num['index']
                if index[0] > self.rows or index[1] > self.cols or index[0] < 0 or index[1] < 0:
                    raise ValidationError(_('Zaznaczono miejsce nie objemowane przez rozkład sali'))
        except TypeError:
            raise ValidationError(_('Niepoprawne wartości lub rozmiar sali'))

    def to_python(self, value):
        """
            Try to convert values in list to ints.
            If it cannot be done change value to None.
            If list is empty or invalid return None.
        """
        print(value)
        raw_layout = value[0]
        self.rows = int(value[1])
        self.cols = int(value[2])
        if len(raw_layout) == 0:
            return None

        # Get minimal values to remove the offset
        min_row_index = min(map(lambda v: int(v) // self.rows, raw_layout))
        min_col_index = min(map(lambda v: int(v) % self.cols, raw_layout))

        layout = list()
        for pos in raw_layout:
            try:
                # Convert to int
                value = int(pos)
                # Get indices without offset
                row = value // self.rows + 1 - min_row_index
                col = value % self.cols + 1 - min_col_index
                # Create dict with real indices and labels
                layout.append({
                    'label': (get_row_label(row), get_col_label(col)),
                    'index': (row, col)
                })
            except ValueError or TypeError:
                layout.append(None)

        layout = super().to_python(layout)
        return layout
