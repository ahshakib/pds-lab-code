import socket

# Client configuration
HOST = '127.0.0.1'  # Server's IP address
PORT = 8080  # Port number
BUFFER_SIZE = 1024  # Buffer size for sending data

# Create a UDP socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open and read the file to be sent
file_name = 'file_to_send.txt'
with open(file_name, 'rb') as file:
    data = file.read(BUFFER_SIZE)
    while data:
        # Send file data in chunks
        client.sendto(data, (HOST, PORT))
        data = file.read(BUFFER_SIZE)

print("File sent successfully!")
client.close()