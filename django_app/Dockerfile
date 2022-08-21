FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /tmp/uwsgi
WORKDIR /usr/src/black_hole
COPY . /usr/src/black_hole
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip install uwsgi
RUN pip install -r requirements.txt
RUN chmod +x /usr/src/black_hole/docker-entrypoint.sh
ENTRYPOINT [ "/usr/src/black_hole/docker-entrypoint.sh" ]
