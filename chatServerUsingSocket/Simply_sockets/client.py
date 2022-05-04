import socket

# provide server address and port, we have to provide public ip address.
HOST = '127.0.0.1'
port = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, port))

# send  messaged
client.send("Hello How are you".encode('utf-8'))

print(client.recv(1024).decode('utf-8'))