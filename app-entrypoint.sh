#!/bin/bash

echo "Apply database migrations with DJANGO_DEBUG=$DJANGO_DEBUG"
python manage.py makemigrations
python manage.py migrate

export ENV_PATH=.env
if [ "$DJANGO_DEBUG" != "True" ]
then
  echo "Apply static files collection ENV_PATH=$ENV_PATH"
  python manage.py collectstatic --noinput
fi

echo "Starting the app"

if [ "$DJANGO_DEBUG" == "True" ]
then
  python manage.py runserver 0.0.0.0:8006
else
  gunicorn --config gunicorn_config.py --access-logfile - config.wsgi
fi