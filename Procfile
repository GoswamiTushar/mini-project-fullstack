web: gunicorn core.wsgi:application --log-file - --log-level debug
web: daphne WR.asgi:application --port $PORT --bind 0.0.0.0 -v2
python manage.py collectstatic --noinput
manage.py migrate
