import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.107', 5056))

def get_message():
    return client_socket.recv(1024).decode()

while True:
    message = get_message()
    print(message)

    if "Выберите позицию (0-8):" in message:
        move = input("Ваш ход (0-8): ")
        client_socket.sendall(move.encode())

    elif "Поздравляем!" in message or "К сожалению" in message:
        break

client_socket.close()
