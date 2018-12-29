release: python manage.py flush --no-input; python manage.py makemigrations; python manage.py migrate;
web: gunicorn app.wsgi --log-file -