from django.apps import AppConfig
from django.conf import settings
import threading
import pika
import json
from black_hole import tasks


class AMQPConsum(threading.Thread):
    def callback(self, ch, method, properties, body):
        tasks.create_product.delay(json.loads(body))

    @staticmethod
    def _get_connection():
        return pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', 
        credentials=pika.PlainCredentials(
            'guest', 'guest',
            )))

    def run(self):
        connection = self._get_connection()
        channel = connection.channel()

        channel.queue_declare(queue='main_django_app')

        channel.basic_consume(on_message_callback=self.callback, queue='main_django_app', auto_ack=False)

        channel.start_consuming()





class AgregatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agregator'
    
    def ready(self):
        consumer = AMQPConsum()
        consumer.daemon = True
        consumer.start()
        pass