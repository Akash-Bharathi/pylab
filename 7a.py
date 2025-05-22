#7(a) Create a client server based chat application where multiple clients can connect to a server and exchange message
#SERVER (Multiclient Chat Server)

import socket
import threading

clients = []

def handle_client(client_socket, address):
    print(f"✅ Accepted connection from {address}")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print(f"❌ Connection from {address} closed.")
                clients.remove(client_socket)
                client_socket.close()
                break
            print(f"📨 Received message from {address}: {message}")
            broadcast(message, client_socket)
        except:
            print(f"⚠️ Error with client {address}. Closing connection.")
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen(5)
print("🚀 Server listening on port 5555...")

# Accept clients
while True:
    client_socket, address = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, address))
    thread.start()

# CLIENT (Chat Client)

import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
            else:
                print("⚠️ Connection closed by server.")
                break
        except:
            print("⚠️ An error occurred while receiving messages.")
            break

def send_messages():
    while True:
        try:
            message = input()
            if message.lower() == 'exit':
                print("🚪 Exiting chat.")
                client_socket.close()
                break
            client_socket.send(message.encode())
        except:
            print("⚠️ An error occurred while sending message.")
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5555))

print("✅ Connected to the chat server. Type and press enter to chat. Type 'exit' to leave.")

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
