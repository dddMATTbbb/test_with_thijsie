import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 514       # Choose a port number

    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one incoming connection

    print(f"Server listening on {host}:{port}")

    connection, address = server_socket.accept()
    with connection:
        print(f"Connection from {address}")
        data = connection.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_server()
