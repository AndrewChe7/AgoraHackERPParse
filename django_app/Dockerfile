FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /tmp/uwsgi
RUN touch /tmp/uwsgi/black_hole.sock
RUN mkdir /sock
RUN chmod -R 666 /sock
COPY black_hole.uwsgi.ini /etc/
WORKDIR /usr/src/black_hole
COPY . /usr/src/black_hole
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip install uwsgi
RUN pip install -r requirements.txt
