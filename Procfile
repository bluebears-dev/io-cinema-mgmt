release: python manage.py migrate; python manage.py loaddata auth cinema content movie_genre ticket_type
web: gunicorn app.wsgi --log-file -