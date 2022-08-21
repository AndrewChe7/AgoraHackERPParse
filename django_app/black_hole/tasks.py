from celery import shared_task
from agregator import models
from agregator import serializers

@shared_task(serializer='json')
def CreateProduct(json_information):
    """Сюда приходит json создать объекты
        по типу:
                Product.objects.create(...)
                """
    pass