FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 0

RUN apk update \
    # psycopg2 dependencies
    && apk add --no-cache --virtual=build-deps gcc musl-dev postgresql-dev \
    && apk add --no-cache \
    postgresql-client

COPY requirements.txt /requirements/
RUN pip install --no-cache-dir -r /requirements/requirements.txt

COPY docker/local/wait-for-postgres.sh /scripts/wait-for-postgres.sh
RUN chmod +x /scripts/wait-for-postgres.sh

COPY docker/local/start /start
RUN chmod +x /start

RUN apk del --purge build-deps && rm -rf /root/.cache /tmp/*

WORKDIR /app/bookstore
