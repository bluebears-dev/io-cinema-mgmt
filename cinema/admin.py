from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from cinema.models import Cinema, Room, Booking
from .models import EmployeeProfile, ClientProfile, Movie, TicketType, Showing, Client
from .forms import ShowingForm


class EmployeeInline(admin.StackedInline):
    """
        Inline form for EmployeeProfile
    """
    model = EmployeeProfile
    can_delete = False


class ClientInline(admin.StackedInline):
    """
        Inline form for ClientProfile
    """
    model = ClientProfile
    can_delete = False


class EmployeeAdmin(BaseUserAdmin):
    """
        User and cinema Client model with user profile form
    """
    inlines = (EmployeeInline,)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(EmployeeAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'is_staff':
            field.initial = True
        return field

    def get_queryset(self, request):
        """
            Return only employees - is_staff flag is set
        :param request:
        :return: filtered QuerySet
        """
        qs = super(EmployeeAdmin, self).get_queryset(request)
        return qs.filter(is_staff=True)


class ClientAdmin(admin.ModelAdmin):
    """
        User and cinema Client model with user profile form
    """
    inlines = (ClientInline,)
    list_display = ('username', 'full_name', 'email')
    fields = ('username', 'first_name', 'last_name', 'email')

    def full_name(self, object):
        """
            Return full name of given user
        :param object: Client model
        :return: full name
        """
        return '{0} {1}'.format(object.first_name, object.last_name)

    full_name.short_description = 'Imię i nazwisko'

    def get_queryset(self, request):
        """
            Return only client - is_staff flag not set
        :param request:
        :return: filtered QuerySet
        """
        qs = super(ClientAdmin, self).get_queryset(request)
        return qs.filter(is_staff=False)


class MovieAdmin(admin.ModelAdmin):
    """
        Movie list with filtering
    """

    list_display = ('title', 'releaseDate', 'producer', 'length')
    list_filter = ('releaseDate', 'producer')


class TicketTypeAdmin(admin.ModelAdmin):
    """
        TicketType list display
    """
    list_display = ('ticketType', 'price')


class ShowingAdmin(admin.ModelAdmin):
    """
        Showing list display and filtering
    """
    list_display = ('movie', 'date', 'hour', 'room', 'audio_type', 'picture_type')
    list_filter = ('movie', 'date', 'room')


class BookingAdmin(admin.ModelAdmin):
    """
        Booking list display and filtering
    """
    list_display = ('showing', 'user', 'state')
    list_filter = ('showing', 'user', 'state')


# Register models (with admin panel models)
admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Showing, ShowingAdmin)
admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)
