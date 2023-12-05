import socket

def start_echo_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Echo server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        data = client_socket.recv(1024)
        while data:
            print(f"Received: {data.decode()}")
            client_socket.sendall(data)
            data = client_socket.recv(1024)

        print(f"Connection with {client_address} closed.")
        client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 5555
    start_echo_server(server_host, server_port)
