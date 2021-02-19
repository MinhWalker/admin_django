#amqps://pzuutqhw:zB2jq4yz1gzYjPSveV5_ZOehu25TzwAx@eagle.rmq.cloudamqp.com/pzuutqhw
import pika, json

params = pika.URLParameters('amqps://pzuutqhw:zB2jq4yz1gzYjPSveV5_ZOehu25TzwAx@eagle.rmq.cloudamqp.com/pzuutqhw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
