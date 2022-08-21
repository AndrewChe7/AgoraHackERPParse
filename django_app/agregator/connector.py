import threading

import pika
from django.conf import settings
from black_hole import tasks


class AMQPConsum(threading.Thread):
    def callback(self, ch, method, properties, body):
        tasks.CreateProduct.delay(body)

    @staticmethod
    def _get_connection():
        parameters = pika.URLParameters('amqp://guest:guest@rabbitmq:5672/%2F')
        return pika.BlockingConnection(parameters)

    def run(self):
        connection = self._get_connection()
        channel = connection.channel()

        channel.queue_declare(queue='main_django_app')
        print('Hello world! :)')

        channel.basic_consume(self.callback, queue='main_django_app')

        channel.start_consuming()