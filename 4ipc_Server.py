import socket
import struct

def server_program():
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 6666))
    server_socket.listen(1)  # Listen for one client
    print("Server is waiting for a connection...")

    # Accept a connection from the client
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    try:
        # Receive two integers from the client
        data = conn.recv(8)  # Expecting two 4-byte integers (8 bytes total)
        a, b = struct.unpack('!ii', data)  # Unpack the data as two integers
        print(f"Received numbers: {a} and {b}")
        print(f"Sum: {a + b}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        conn.close()
        server_socket.close()
        print("Server closed.")

if __name__ == "__main__":
    server_program()
