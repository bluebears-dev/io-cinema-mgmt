from django.contrib import admin

from cinema.models import TicketType, Booking


class TicketTypeAdmin(admin.ModelAdmin):
    """
        TicketType list display
    """
    list_display = ('name', 'price')


admin.site.register(TicketType, TicketTypeAdmin)
