import socket

# Server configuration
HOST = '127.0.0.1'  # Loopback IP address for local testing
PORT = 8080  # Port number
BUFFER_SIZE = 1024  # Buffer size for receiving data

# Create a UDP socket object
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the host and port
server.bind((HOST, PORT))

print("Server is listening for file transfer...")

ok = 0
# Receive the file data
with open('received_file.txt', 'wb') as file:
    data, client_address = server.recvfrom(BUFFER_SIZE)
    file.write(data)
    file.close()
    print("File transfer complete!")
    server.close()