import socket
import os


def send_file():
    host = "192.168.1.107"
    port = 5050

    filename = input("Enter file path to send: ")
    if not os.path.exists(filename):
        print("File not found!")
        return

    filesize = os.path.getsize(filename)
    basename = os.path.basename(filename)

    print(f"Attempting to send {basename} ({filesize} bytes)")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        file_info = f"{basename}|{filesize}"
        client.send(file_info.encode())
        response = client.recv(1024).decode()
        if response == "confirm":
            confirmation = input(f"Receiver asks to send {basename}. Confirm? (yes/no): ")
            client.send(confirmation.encode())

            if confirmation != "yes":
                print("Transfer canceled")
                return

            response = client.recv(1024).decode()
            if response == "start":
                print("Sending file...")

                with open(filename, "rb") as f:
                    while True:
                        bytes_read = f.read(4096)
                        if not bytes_read:
                            break
                        client.sendall(bytes_read)
                response = client.recv(1024).decode()
                print(f"Server response: {response}")

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client.close()


if __name__ == "__main__":
    send_file()