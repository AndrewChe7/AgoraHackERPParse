FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /parse_microservice
COPY requirements.txt /parse_microservice/requirements.txt
RUN pip install -r requirements.txt
COPY . /parse_microservice