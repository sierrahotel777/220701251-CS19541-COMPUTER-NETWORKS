import socket

def tcp_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("TCP server is waiting for a connection...")
    connection, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    try:
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
                connection.sendall(data)  # Echo back the received data
            else:
                break
    finally:
        connection.close()

if __name__ == "__main__":
    tcp_server()
