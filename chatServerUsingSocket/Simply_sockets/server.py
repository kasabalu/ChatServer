import socket

Host = '127.0.0.1'
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - different types of sockets INternet, Bluetooth, Infrared, AF_INET is for Internet
#sock_STREAM is for TCP connection , SOCK_DGRAM is for UDP connection.

# bind the server with host and port
server.bind((Host, port))

server.listen(5) # limit the number of waiting connections, it is optional

while True:
    #server.accept  return two values, one is socket  for further communication, ipadress
    communication_socket, ipaddress =  server.accept()
    print("connected to {}".format(ipaddress))

    # to recieve message
    message = communication_socket.recv(1024).decode('utf-8')
    # we have to decode the message, message transfered in bytes
    print("message from client {}".format(message))
    communication_socket.send("got your message".encode('utf-8'))

    # close the connection
    communication_socket.close()
    print("connection has been closed")




