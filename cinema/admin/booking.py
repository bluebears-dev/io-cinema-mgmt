from django.contrib import admin

from cinema.models import TicketType, Booking


class TicketTypeAdmin(admin.ModelAdmin):
    """
        TicketType list display
    """
    list_display = ('name', 'price')


class BookingAdmin(admin.ModelAdmin):
    """
        Booking list display and filtering
    """
    list_display = ('showing', 'user', 'state')
    list_filter = ('showing', 'user', 'state')


admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Booking, BookingAdmin)
