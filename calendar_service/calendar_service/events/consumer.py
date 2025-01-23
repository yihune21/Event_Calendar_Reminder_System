import pika
import json
import threading

class Consumer:
    def __init__(self, queue_name='user_queue', host='localhost'):
        self.queue_name = queue_name
        self.host = host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        self.message = None
        self.message_event = threading.Event()

    def callback(self, ch, method, properties, body):
        print(f" [x] Received {body}")
        try:
            self.message = json.loads(body)
            print(self.message)
        except json.JSONDecodeError:
            print("Received message is not in JSON format")
            self.message = body.decode('utf-8')  # Store the raw message as a string
        self.message_event.set()  # Signal that the message has been received

    def start_consuming(self):
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=self.callback,
                                   auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def wait_for_message(self):
        self.message_event.wait()  # Wait until the message is received
        return self.message

    def get_latest_message(self):
        if self.message_event.is_set():
            return self.message
        return None

if __name__ == "__main__":
    consumer = Consumer()
    threading.Thread(target=consumer.start_consuming).start()
    message = consumer.wait_for_message()
    print(f"Processed message: {message}")