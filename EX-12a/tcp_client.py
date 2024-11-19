import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    try:
        message = input("Enter message to send: ")
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    tcp_client()
