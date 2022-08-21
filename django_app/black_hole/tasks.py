from celery import shared_task


from django.apps import apps

@shared_task
def crate_product(json_payload):
    model = apps.get_model('agregator', 'Product')
    model = apps.get_model('agregator', 'MeasureUnit')
    model = apps.get_model('agregator', 'Category')
    pass