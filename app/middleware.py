import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import redirect_to_login

from app import settings


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            current_time = datetime.datetime.now()
            if 'last_login' in request:
                delta_last_login = (current_time - request.session['last_login']).seconds
                if delta_last_login > settings.SESSION_TIMEOUT:
                    logout(request)
                    messages.add_message(request, messages.ERROR, 'Your session has been timed out.')
                    return redirect_to_login(next=request.path)
                else:
                    request.session['last_login'] = current_time
        return None
