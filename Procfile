release: python manage.py migrate
web: gunicorn -t 60 open_show_off.wsgi --log-file -