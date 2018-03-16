import zmq
from threading import Thread
import sys
import time

clientName= sys.argv[1]
# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"

sender = context.socket(zmq.PUSH)
sender.connect("tcp://127.0.0.1:5679")
print('User {} connected to the char server'.format(clientName))

def subscriber():
    sock = context.socket(zmq.SUB)
    sock.connect("tcp://127.0.0.1:5680")
    sock.setsockopt_string(zmq.SUBSCRIBE, "")

    while True:
        time.sleep(1)
        pub_message= sock.recv().decode()
        if(pub_message):
            if ("[{}]:".format(clientName) not in pub_message):
                print("\n"+ pub_message+"\n[" + clientName + "]>", end="")

thread = Thread(target=subscriber)
thread.start()

while True:
    message = input("[{0}] > ".format(clientName))
    message = "[%s]:  %s" % (clientName, message)
    sender.send(message.encode())

