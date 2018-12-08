import datetime

from django.contrib.auth import logout, login

from app import settings


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        if request.user.is_authenticated():
            current_time = datetime.datetime.now()
            if 'last_login' in request:
                delta_last_login = (current_time - request.session['last_login']).seconds
                if delta_last_login > settings.SESSION_TIMEOUT:
                    logout(request, login.html)
            else:
                request.session['last_login'] = current_time
        return None
