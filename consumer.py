import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://pzuutqhw:zB2jq4yz1gzYjPSveV5_ZOehu25TzwAx@eagle.rmq.cloudamqp.com/pzuutqhw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')

    if properties.content_type == 'product_liked':
        id = json.loads(body)
        print(id)
        product = Product.objects.get(id=id)
        product.likes = product.likes + 1
        product.save()
        print('Product likes increased!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Stated Consuming')

channel.start_consuming()

channel.close()