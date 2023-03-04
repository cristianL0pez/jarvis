#!/bin/sh
python manage.py migrate 
## en el host:sudo chown -R $USER:$USER .
python manage.py collectstatic --no-input
gunicorn jarvis_core.wsgi:application --bind 0.0.0.0:8000


