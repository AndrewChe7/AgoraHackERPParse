import json
import pika
import toml
import xmltodict
import xmlschema

cfg = None
schema = None

def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    if not validator(body):
        print("Invalid xml")
        return
    res = parse_data(body)
    res = convert_to_unified_format(res)
    for product in res['Nomenclature']:
        ch.basic_publish(exchange='', routing_key='main_django_app', body=json.dumps(product))
    ch.basic_ack(delivery_tag=method.delivery_tag)

def parse_data(data: str) -> dict:
    return xmltodict.parse(data)

#inputs raw data as str
def validator(xml) -> bool:
    global cfg, schema
    xml = xml.replace(cfg['parser']['old_header'], cfg['parser']['new_header'])
    return schema.is_valid(xml)

def convert_to_unified_format(data: dict) -> dict:
    global cfg
    try:
        keys_rename_dict = json.loads(cfg['parser']['rename_dict'].replace('\n', '').replace("'", '"'))
        dict_iter_template = json.loads(cfg['parser']['iter_template_dict'].replace('\n', '').replace("'", '"'))
    except:
        print("incorrect .toml file dict data")

    # renaming module
    def walk_and_rename(dict_to_change: dict, dict_template: dict):
        for key in dict_template.keys():
            try:
                dict_to_change[keys_rename_dict[key]] = dict_to_change.pop(key)
                if type(dict_to_change[keys_rename_dict[key]]) is list:
                    for sub_dict in dict_to_change[keys_rename_dict[key]]:
                        walk_and_rename(sub_dict, dict_template[key])
                elif type(dict_to_change[keys_rename_dict[key]]) is dict:
                    walk_and_rename(dict_to_change[keys_rename_dict[key]], dict_template[key])
                else:
                    pass
            except KeyError:
                print("No key named {} found in file".format(key))

    for key in cfg['parser']['dewrap_keys']:
        data = data[key]

    for key in cfg['parser']['ignore_keys']:
        try:
            data.pop(key)
        except KeyError:
            continue

    walk_and_rename(data, dict_iter_template)
    return data

def main():
    global cfg, schema
    print('Start parsing microservice')
    with open('config.toml', 'r') as f:
        config = toml.load(f)
        cfg = config
    with open(config['parser']['schema_path'], 'r') as f:
        schema_str = f.read()
    schema = xmlschema.XMLSchema(schema_str)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config['rabbitmq']['host'], 
        credentials=pika.PlainCredentials(
            config['rabbitmq']['user'], config['rabbitmq']['password']
            )))
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