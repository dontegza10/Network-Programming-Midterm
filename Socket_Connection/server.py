
import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 5000

def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Allow the address to be reused
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the host and port
        server_socket.bind((HOST, PORT))

        # Listen for incoming connections
        server_socket.listen(1)

        print(f"Server listening on {HOST}:{PORT}")
        print("Waiting for a client connection...")

        # Accept an incoming connection
        connection, address = server_socket.accept()

        with connection:
            print(f"Connected to client: {address}")

            while True:
                # Receive data from client
                data = connection.recv(1024)

                if not data:
                    print("Client disconnected.")
                    break

                message = data.decode("utf-8")
                print(f"Client says: {message}")

                # Process and respond to the message
                response = f"Server received: {message}"
                connection.sendall(response.encode("utf-8"))

                if message.strip().lower() == "exit":
                    print("Closing connection...")
                    break

    except OSError as error:
        print(f"Server error: {error}")

    except KeyboardInterrupt:
        print("\nServer interrupted by user.")

    finally:
        server_socket.close()
        print("Server socket closed.")


if __name__ == "__main__":
    start_server()
