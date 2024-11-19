import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Server: {message}")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))
    print("Connected to the chat server.")
    
    # Start a thread to listen for messages from the server
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()