import socket

def start_echo_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Enter a message to be echoed (type 'exit' to quit): ")
    while message.lower() != 'exit':
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
        message = input("Enter another message (type 'exit' to quit): ")

    client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 5555
    start_echo_client(server_host, server_port)
