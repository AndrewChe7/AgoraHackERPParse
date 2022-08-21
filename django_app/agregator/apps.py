from django.apps import AppConfig
from django.conf import settings
import threading
import pika
import json
#from black_hole import tasks

def create_product(json_information):
    pass

class AMQPConsum(threading.Thread):
    def callback(self, ch, method, properties, body):
        create_product(json.loads(body))

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





class AgregatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agregator'
    
    def ready(self):
        consumer = AMQPConsum()
        consumer.daemon = True
        consumer.start()
        pass