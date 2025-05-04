import socket
import threading

clients = {}  # Словарь клиентов: {socket: name}


def handle_client(client_socket, client_address):
    """Обрабатываем клиента и рассылаем его сообщения другим"""
    print(f"Новое подключение: {client_address}")

    try:
        # Получаем имя клиента
        name = client_socket.recv(1024).decode()
        clients[client_socket] = name
        welcome_msg = f"Добро пожаловать, {name}!"
        client_socket.sendall(welcome_msg.encode())

        # Оповещаем всех о новом участнике
        broadcast(f"{name} присоединился к чату!", client_socket)

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # Клиент отключился

            print(f"Сообщение от {name}: {data}")
            broadcast(f"{name}: {data}", client_socket)

    except (ConnectionResetError, ConnectionAbortedError):
        print(f"Клиент {client_address} отключился")
    finally:
        if client_socket in clients:
            name = clients[client_socket]
            broadcast(f"{name} покинул чат.", client_socket)
            del clients[client_socket]
        client_socket.close()
        print(f"Клиент {client_address} отключен")


def broadcast(message, sender_socket=None):
    """Отправляем сообщение всем клиентам, кроме отправителя"""
    for client in list(clients.keys()):
        if client != sender_socket:
            try:
                client.sendall(message.encode())
            except:
                del clients[client]
                client.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("192.168.1.107", 5052))
    server_socket.listen(5)
    print("Чат запущен. Ожидаем подключений...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True
            client_thread.start()
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()