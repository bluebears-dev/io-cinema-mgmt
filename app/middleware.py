import datetime

import pytz
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login

from app import settings


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            current_time = datetime.datetime.now(pytz.utc)
            current_user = User.objects.get(pk=request.user.id)
            delta_last_login = (current_time - current_user.last_login).seconds
            if delta_last_login > settings.SESSION_TIMEOUT:
                logout(request)
                messages.add_message(request, messages.ERROR, 'Your session has been timed out.')
                return redirect_to_login(next=request.path)
            else:
                current_user.last_login = current_time
                current_user.save()
        return None
