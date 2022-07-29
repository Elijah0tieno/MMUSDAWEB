release: python manage.py migrate  --run-syncdb
web: gunicorn mmusdaweb.wsgi:application --log-file -
