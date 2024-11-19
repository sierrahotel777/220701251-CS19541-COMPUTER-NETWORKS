import socket

def start_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP Server running on {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)  # Buffer size is 1024 bytes
            print(f"Received message from {addr}: {data.decode()}")
            s.sendto(b'Pong', addr)  # Respond with 'Pong'

if __name__ == "__main__":
    start_server()
