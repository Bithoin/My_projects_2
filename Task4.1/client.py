import socket
import threading

def receive_messages(client_socket):
    """Постоянно слушаем входящие сообщения"""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print("\nСоединение с сервером разорвано")
                break
            print(f"\n{message}\n> ", end="")
        except:
            print("\nОшибка соединения")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.1.107", 5052))

    print("Вы подключены к чату. Введите имя:")
    name = input("> ")
    client_socket.sendall(name.encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    try:
        while True:
            message = input("> ")
            if message.lower() == "выход":
                break
            client_socket.sendall(message.encode())
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()