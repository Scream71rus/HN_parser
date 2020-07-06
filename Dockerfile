FROM python:3.6-alpine3.8

RUN apk update && apk upgrade && \
    apk add --no-cache \
        build-base \
        gcc \
        git \
        postgresql-client \
        postgresql-dev

RUN mkdir /home/application
COPY ./ /home/application/
WORKDIR /home/application

RUN pip3 install -r requirements

RUN chmod +x ./docker-entrypoint.sh

ENV PGPASSWORD=admin

ENTRYPOINT ["/home/application/docker-entrypoint.sh"]
