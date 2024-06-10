FROM python:3.12-slim

WORKDIR /api

RUN apt-get update && apt-get install -y build-essential libpq-dev

RUN addgroup -S app && adduser -S app -G app

ADD . /api

RUN chown api:api -R  /tmp /api

USER api

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