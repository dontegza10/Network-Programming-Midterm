
import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 5000

def start_client():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Set connection timeout
        client_socket.settimeout(5)

        # Connect to the server
        client_socket.connect((HOST, PORT))

        print(f"Successfully connected to server at {HOST}:{PORT}")
        print("Type messages to send to the server.")
        print("Type 'exit' to disconnect.")

        while True:
            message = input("Enter message: ")

            # Send message to server
            client_socket.sendall(message.encode("utf-8"))

            # Receive server response
            response = client_socket.recv(1024)

            if not response:
                print("Server disconnected.")
                break

            print(f"Server response: {response.decode('utf-8')}")

            if message.strip().lower() == "exit":
                break

    except ConnectionRefusedError:
        print("Connection failed: Server is not running.")

    except socket.timeout:
        print("Connection timed out.")

    except OSError as error:
        print(f"Client error: {error}")

    finally:
        client_socket.close()
        print("Client socket closed.")


if __name__ == "__main__":
    start_client()
