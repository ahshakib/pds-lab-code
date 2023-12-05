import socket

# Server configuration
HOST = '127.0.0.1'  # Loopback IP address for local testing
PORT = 8080  # Port number

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server.bind((HOST, PORT))

# Listen for incoming connections (up to 5 clients)
server.listen(5)
print("Server is listening...")

# Accept incoming connections
client_socket, address = server.accept()
print(f"Connection from {address} has been established.")

# Receive data from the client
while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Received message: {data}")

client_socket.close()