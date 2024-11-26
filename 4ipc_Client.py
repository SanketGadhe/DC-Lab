import socket
import struct

def client_program():
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 6666))
    print("Connected to the server.")

    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        data = struct.pack('!ii', a, b)  
        client_socket.send(data)
        print("Data sent to the server.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        client_socket.close()
        print("Client closed.")

if __name__ == "__main__":
    client_program()
