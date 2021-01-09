import pika
import time

sleepTime = 20
print("Sleeping for ", sleepTime, " seconds.")
time.sleep(sleepTime)

print("Connecting to server ...")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()
channel.queue_declare(queue="hello_queue", durable=True)

print("Waiting for messages.")


def callback(ch, method, properties, body):
    print("Received %s" % body)
    name = body.decode()

    if name:
        print("Hey %s" % name)
    else:
        print("Sorry, no name ")

    print("Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="hello_queue", on_message_callback=callback)
channel.start_consuming()
