import socket
import time

def ping_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.settimeout(2)  # Set a timeout for the response
            start = time.time()  # Record the start time
            s.sendto(b'Ping', (host, port))  # Send 'Ping' to the server
            data, addr = s.recvfrom(1024)  # Wait for a response
            end = time.time()  # Record the end time
            print(f"Received {data.decode()} from {addr} in {end - start:.2f} seconds")
        except socket.timeout:
            print("Request timed out")

if __name__ == "__main__":
    ping_server()
