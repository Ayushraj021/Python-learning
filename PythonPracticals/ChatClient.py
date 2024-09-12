import socket

# Client configuration
HOST = '127.0.0.1'
PORT = 12345

def start_client():
    """Start the client."""
    # Set up client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to server")

    while True:
        # Send message to server
        message = input("Enter message: ")
        client_socket.sendall(message.encode())
        if message.lower() == "exit":
            break

        # Receive echoed message from server
        echoed_message = client_socket.recv(1024)
        print(f"Received from server: {echoed_message.decode()}")

    # Close client socket
    client_socket.close()
    print("Connection with server closed")

# Start the client
start_client()
