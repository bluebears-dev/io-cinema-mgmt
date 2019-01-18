from django import forms
from django.contrib import admin
from django.utils.translation import gettext as _

from cinema.fields import LayoutField
from .models import Showing, Room, EmployeeProfile, ClientProfile


class EmployeeInline(admin.StackedInline):
    """
        Inline form for EmployeeProfile
    """
    model = EmployeeProfile
    can_delete = False
    extra = 1
    max_num = 1
    min_num = 1


class ClientInline(admin.StackedInline):
    """
        Inline form for ClientProfile
    """
    model = ClientProfile
    can_delete = False
    extra = 1
    max_num = 1
    min_num = 1


class ShowingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShowingForm, self).__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.all()

    class Meta:
        model = Showing
        fields = ('movie', 'date', 'hour', 'room', 'audio_type', 'picture_type')


class RoomForm(forms.ModelForm):
    """
        Room form definition
    """
    rows = forms.IntegerField(label=_('Ilość rzędów'), min_value=1, max_value=26, initial=1)
    cols = forms.IntegerField(label=_('Ilość kolumn'), min_value=1, max_value=70, initial=1)
    layout = LayoutField(label=_('Rozkład sali'))

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super(RoomForm, self).__init__(*args, **kwargs)
        # if editing load instance values
        if instance:
            self.fields['rows'].initial = instance.rows
            self.fields['cols'].initial = instance.cols
            self.fields['layout'].initial = instance.raw_layout
            print(instance.raw_layout)

    class Meta:
        model = Room
        fields = ('name', 'cinema', 'rows', 'cols', 'layout',)
