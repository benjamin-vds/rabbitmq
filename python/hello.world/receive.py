#!/usr/bin/env python
import pika, sys,os
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    #connect to channel of hello we don't know if the que already exist
    channel.queue_declare(queue='hello')

    # this is part of the Pika library so we will read it and print it to the screen
    def callback(ch, method, properties, body):
        print(f" [x] Received by python {body}")
        
    # the callback will get the message from the hello queue
    channel.basic_consume(queue='hello',
                        auto_ack=True,
                        on_message_callback=callback)

    # we will set up a never ending loop because we are waiting for the message
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
