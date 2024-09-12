import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

def handle_client(client_socket, addr):
    """Handle client connections."""
    print(f"Connected to {addr}")
    while True:
        try:
            # Receive message from client
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received from client: {message}")

            # Echo the message back to client
            client_socket.sendall(data)
        except Exception as e:
            print(f"Error: {e}")
            break

    # Close client socket
    client_socket.close()
    print(f"Connection with {addr} closed")

def start_server():
    """Start the server."""
    # Set up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        # Handle client connection in a new thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

# Start the server
start_server()
