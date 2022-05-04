import socket
import threading

# Choosing User Name
username = input("Choose your User Name: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55556))


def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'USERNAME' Send User-Name
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(username, input(''))
        client.send(message.encode('utf-8'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()