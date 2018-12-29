release: mv ./static/index.html .; python manage.py makemigrations; python manage.py migrate;
web: gunicorn app.wsgi --log-file -