import socket

# Client configuration
HOST = '127.0.0.1'  # Loopback IP address
PORT = 8080  # Port number

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((HOST, PORT))

send_data = input("Enter a message: ")

# Send data to the server
client.sendall(send_data.encode('utf-8'))

client.close()