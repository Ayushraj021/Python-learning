import tkinter as tk
from tkinter import messagebox
import socket

# Client configuration
HOST = '127.0.0.1'
PORT = 12345

def login():
    """Send username and password to the server for authentication."""
    username = username_entry.get()
    password = password_entry.get()

    # Set up client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Send username and password to server
    client_socket.sendall(username.encode())
    client_socket.sendall(password.encode())

    # Receive authentication result from server
    auth_result = client_socket.recv(1024).decode()

    # Display result message
    messagebox.showinfo("Authentication Result", auth_result)

    client_socket.close()

# Create the main window
window = tk.Tk()
window.title("Login Screen")

# Username label and entry
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password label and entry
password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login button
login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
window.mainloop()
