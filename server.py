import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://127.0.0.1:5679")
broadcaster = context.socket(zmq.PUB)
broadcaster.bind("tcp://127.0.0.1:5680")

# Run server
while True:
    message = receiver.recv()
    broadcaster.send(message)
    print("[Server] Echo: " + message.decode())