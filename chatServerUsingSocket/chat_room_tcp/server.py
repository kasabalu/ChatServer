import socket
import threading

# we need thereading to handle each client in one thread, so that we can handle many clients at once

# Connection Data
host = '127.0.0.1'
port = 55556

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For clients and their user names
clients = []
usernames = []


# send message all connected clients.
def broadcast(msg):
    for client in clients:
        client.send(msg)
        # here client is client socket for communication returned while accept call

# handling messages from client, below method will run in multithreading fashion.
def handler(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast('{} left!'.format(username).encode('utf-8'))
            usernames.remove(username)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('USERNAME'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        # Print And Broadcast Nickname
        print("username is {}".format(username))
        broadcast("{} joined!".format(username).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handler, args=(client,))
        thread.start()

print("server listening")
receive()