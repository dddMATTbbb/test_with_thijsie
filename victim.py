import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '85.148.134.70'  # Use the server's IP address or hostname
    port = 514       # Use the same port number as the server

    client_socket.connect((host, port))

    message = "Hello"
    client_socket.sendall(message.encode('utf-8'))
    print(f"Sent: {message}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
