FROM python:3.7-alpine

RUN apk update \
    && apk add --no-cache \
    postgresql-client

COPY docker/local/wait-for-postgres.sh /scripts/wait-for-postgres.sh
RUN chmod +x /scripts/wait-for-postgres.sh

COPY docker/local/start /start
RUN chmod +x /start
