#7(b) Create a client server based chat application where multiple clients can connect to a server 
#7(b) Create a client server based chat application where multiple clients can connect to a server 

#SERVER (with Nicknames Support)
import socket
import threading

# Server config
HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message, sender_client=None):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                # Handle broken connections
                if client in clients:
                    clients.remove(client)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            client.close()
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} left the chat.".encode('utf-8'))
            break

def receive():
    print(f"🚀 Server is running on {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        print(f"✅ Connected with {str(address)}")

        client.send("NICKNAME".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        print(f" Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send(" Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()



#CLIENT (with Nickname Support)

import socket
import threading

# Server config
HOST = '127.0.0.1'
PORT = 12345

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NICKNAME":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print(" An error occurred!")
            client.close()
            break

def write():
    while True:
        msg = f"{nickname}: {input('')}"
        try:
            client.send(msg.encode('utf-8'))
        except:
            print(" Message failed to send. Exiting...")
            break

# Start threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
