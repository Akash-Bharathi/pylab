#7(a) Create a client server based chat application where multiple clients can connect to a server and exchange message
#SERVER (Multiclient Chat Server)

import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            print(f"Connection from {address} closed.")
            break
        print(f"Received message from {address}: {message}")
        broadcast(message)

def broadcast(message):
    for client in clients:
        client.send(message.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen(5)
print("Server listening on port 5555...")
clients = []

while True:
    client_socket, address = server.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()




#client

import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("An error occurred while receiving messages.")
            break

def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5555))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
