from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from cinema.models import Cinema, Room, Booking, Ticket
from .models import UserProfile, Movie, TicketType, Showing


class UserInline(admin.StackedInline):
	model = UserProfile
	can_delete = False


class UserAdmin(BaseUserAdmin):
	"""
		User and cinema Client model with user profile form
	"""
	inlines = (UserInline,)


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


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Showing, ShowingAdmin)
admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)
