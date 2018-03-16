# GroupChat-using-ZeroMQ

This is a group chat client/server implementation to explore the base ZeroMQ API and some of the higher level patterns. <br />

The client uses multithreading and ZeroMQ's asynchronous I/O model to separately update the message text input interfaces, communicate between components, and send messages and receive replies from the server. <br />

The server simply exposes a port for incoming messages and broadcasts them to all currently connected clients. <br />


**ZeroMQ** is a high-performance asynchronous messaging library, aimed at use in distributed or concurrent applications. <br />
It provides a message queue, but unlike message-oriented middleware, a ZeroMQ system can run without a dedicated message broker. <br />

### How to Setup

```sh
virtualenv -p python3 my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt
```

### How to run Chat server

```sh
python3 server.py
```

### How to run a Chat client

```sh
python3 client.py [username]
```

__Expected Output__

# Bob's client
```sh
python3 client.py Bob
User[Bob] Connected to the chat server.
[Bob] > 
[Alice]: Hi from Alice.
[Smith]: Hi from Smith.
[Bob] > Hello World
```

# Alice's client
```sh
python3 client.py Bob
User[Alice] Connected to the chat server. 
[Alice] > Hi from Alice.
[Smith]: Hi from Smith.
[Bob]: Hello World
```
