FROM python:3.11-alpine

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 6183


RUN apk update && apk upgrade
RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN chown -R django-user:django-user /app
RUN rm -rf /tmp
USER django-user