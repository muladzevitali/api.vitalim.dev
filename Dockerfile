FROM python:3.12-slim

WORKDIR /api

RUN apt-get update && apt-get install -y build-essential libpq-dev

RUN useradd --create-home api
RUN chown api:api -R  /tmp /api

USER api

COPY --chown=api:api ./requirements.txt /api

ENV PYTHONUNBUFFERED="${PYTHONUNBUFFERED}" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/api/.local/bin" \
    USER="api"

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

## copy project
COPY --chown=api:api ./ /api
COPY --chown=api:api ./.env /api/.env
COPY --chown=api:api ./app-entrypoint.sh /

RUN chmod u+x /app-entrypoint.sh

EXPOSE 8006
CMD sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --config gunicorn_config.py --access-logfile - config.wsgi"