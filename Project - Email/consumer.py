import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue with the same durable setting as before (durable=True)
channel.queue_declare(queue='test_queue', durable=True)

# Callback function to process received messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

# Set up consuming
channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
