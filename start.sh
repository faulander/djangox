#!/bin/bash
python manage.py collectstatic --noinput
#python manage.py run_huey &
gunicorn djangox_project.wsgi:application -w 2 -b :8000
exec "$@"
