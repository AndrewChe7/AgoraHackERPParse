FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/black_hole
COPY . /usr/src/black_hole
RUN apk add python3.10-dev build-base linux-headers pcre-dev
RUN pip install uwsgi
RUN pip install -r requirements.txt
