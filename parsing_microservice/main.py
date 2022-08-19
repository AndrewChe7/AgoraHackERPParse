import json
import pika
import toml
import xmltodict

def callback(ch, method, properties, body):
    res = parse_data(body)
    res = convert_to_unified_format(res)
    ch.basic_publish(exchange='', routing_key='main_django_app', body=json.dumps(res))
    ch.basic_ack(delivery_tag=method.delivery_tag)

def parse_data(data: str) -> dict:
    return xmltodict.parse(str)

def convert_to_unified_format(data: dict) -> dict:
    #TODO: make converter
    return {}

def main():
    with open('config.toml', 'r') as f:
        config = toml.load(f)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=config['rabbitmq']['host']))
    channel = connection.channel()
    queue_name = 'parser_queue_{}'.format(config['parser_id'])
    channel.queue_declare(queue=queue_name)
    channel.queue_declare(queue='main_django_app')
    channel.basic_consume(on_message_callback=callback, queue=queue_name, auto_ack=False)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped')