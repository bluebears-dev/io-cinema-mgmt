from django import forms
from django.contrib import admin

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
        print(self.user)
        self.fields['room'].queryset = Room.objects.filter(cinema=1)

    class Meta:
        model = Showing
        fields = ('movie', 'date', 'hour', 'room', 'audio_type', 'picture_type')
