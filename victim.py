import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '85.148.134.70'
    port = 514

    client_socket.connect((host, port))

    message = "Hello"
    client_socket.send(message.encode('utf-8'))
    print(f"Sent: {message}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
