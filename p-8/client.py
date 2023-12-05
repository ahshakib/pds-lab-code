import socket

def start_udp_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Enter a message to be sent (type 'exit' to quit): ")
    while message.lower() != 'exit':
        client_socket.sendto(message.encode(), (server_host, server_port))
        data, _ = client_socket.recvfrom(1024)
        print(f"Received from server: {data.decode()}")
        message = input("Enter another message (type 'exit' to quit): ")

    client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 5555
    start_udp_client(server_host, server_port)
