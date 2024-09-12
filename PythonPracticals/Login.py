import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 12345
USERNAME = "client"
PASSWORD = "server"

def authenticate(username, password):
    """Authenticate the client."""
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server is listening...")

while True:
    # Accept incoming connection
    client_socket, addr = server_socket.accept()
    print("Connected to", addr)

    # Receive username and password from client
    username = client_socket.recv(1024).decode()
    password = client_socket.recv(1024).decode()

    # Authenticate
    if authenticate(username, password):
        client_socket.sendall(b"Authenticated")
    else:
        client_socket.sendall(b"Authentication failed")

    client_socket.close()
