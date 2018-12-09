from django.contrib import admin

from cinema.models import Cinema, Showing, Room
from cinema.forms import ShowingForm


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
        return queryset.filter(author=request.user)


admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Showing, ShowingAdmin)
