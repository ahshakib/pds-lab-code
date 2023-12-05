import socket

def start_udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP server is listening on {host}:{port}")

    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            print(f"Received from {client_address}: {data.decode()}")
            server_socket.sendto(data, client_address)
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 5555
    start_udp_server(server_host, server_port)
