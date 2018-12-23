from django import forms
from django.contrib import admin

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
    rows = forms.IntegerField(min_value=1, max_value=70)
    cols = forms.IntegerField(min_value=1, max_value=70)
    layout = LayoutField()

    class Meta:
        model = Room
        fields = "__all__"
