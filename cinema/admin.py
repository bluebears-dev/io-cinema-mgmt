from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserInline(admin.StackedInline):
  model = UserProfile
  can_delete = False

class UserAdmin(BaseUserAdmin):
  """
  User and cinema Client model with user profile form
  """
  inlines = (UserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
