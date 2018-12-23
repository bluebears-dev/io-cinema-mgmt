import json

from django.contrib import admin

from cinema.forms import ShowingForm, RoomForm
from cinema.models import Cinema, Showing, Room


class ShowingAdmin(admin.ModelAdmin):
    """
        Showing list display and filtering
    """
    form = ShowingForm
    list_display = ('movie', 'date', 'hour', 'room', 'audio_type', 'picture_type')
    list_filter = ('movie', 'date', 'room')

    def get_form(self, request, *args, **kwargs):
        form = super(ShowingAdmin, self).get_form(request, *args, **kwargs)
        form.user = request.user
        return form

    def get_queryset(self, request):
        queryset = super(ShowingAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset


class RoomAdmin(admin.ModelAdmin):
    """
        Room admin panel form and display
    """
    form = RoomForm

    def save_model(self, request, obj, form, change):
        obj.json_layout = json.dumps(form.cleaned_data.get('layout'))
        # Recalculate rows and columns because of offset removing
        obj.rows = max(map(lambda v: v['index'][0], form.cleaned_data.get('layout')))
        obj.cols = max(map(lambda v: v['index'][1], form.cleaned_data.get('layout')))
        super().save_model(request, obj, form, change)


admin.site.register(Cinema)
admin.site.register(Room, RoomAdmin)
admin.site.register(Showing, ShowingAdmin)
