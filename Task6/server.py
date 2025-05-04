import socket
import os
import threading


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    try:
        file_info = conn.recv(1024).decode()
        filename, filesize = file_info.split('|')
        filesize = int(filesize)

        print(f"[{addr}] Request to send file: {filename} ({filesize} bytes)")

        conn.send(b"confirm")

        confirmation = conn.recv(1024).decode()
        if confirmation != "yes":
            print(f"[{addr}] Transfer canceled by receiver")
            conn.send(b"Transfer canceled")
            return

        conn.send(b"start")
        print(f"[{addr}] Starting file transfer...")

        if not os.path.exists("received_files"):
            os.makedirs("received_files")

        filepath = os.path.join("received_files", filename)

        with open(filepath, "wb") as f:
            bytes_received = 0
            while bytes_received < filesize:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
                bytes_received += len(data)

        print(f"[{addr}] File received successfully: {filename}")
        conn.send(b"File received successfully")

    except Exception as e:
        print(f"[ERROR] {addr}: {str(e)}")
        conn.send(f"Error: {str(e)}".encode())
    finally:
        conn.close()


def start_server():
    host = "192.168.1.107"
    port = 5050

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"[SERVER] Listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    print("[STARTING] Server is starting...")
    start_server()