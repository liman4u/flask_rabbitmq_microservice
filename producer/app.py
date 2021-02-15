from flask import Flask
import pika

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


@app.route('/hello/<name>')
def hello(name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='hello_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='hello_queue',
        body=name,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()
    return "Sent: %s" % name


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
