web: gunicorn core.wsgi:application --log-file - --log-level debug
web: daphne core.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=core.settings -v2
python manage.py collectstatic --noinput
manage.py migrate
