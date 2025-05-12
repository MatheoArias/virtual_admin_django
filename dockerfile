FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /virtual_admin

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    libffi-dev \
    libpq \
    libjpeg-turbo-dev \
    zlib-dev

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY ./ ./

RUN python manage.py makemigrations
