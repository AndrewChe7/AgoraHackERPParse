from django.apps import AppConfig
from django.conf import settings
""" Вот этот конфиг нужно подружить с AMQPConsum"""
#from .connector import AMQPConsum





class AgregatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agregator'
    
    def ready(self):
        """consumer = AMQPConsuming()
        consumer.daemon = True
        consumer.start()"""
        pass