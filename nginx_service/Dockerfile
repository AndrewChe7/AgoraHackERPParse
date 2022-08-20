FROM nginx
RUN mkdir /usr/src/black_hole
RUN mkdir /sock
RUN touch /sock/django.sock

COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./django.nginx.conf /etc/nginx/sites-available/django.nginx.conf
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/django.nginx.conf /etc/nginx/sites-enabled/
CMD ["nginx", "-g", "daemon off;"]
