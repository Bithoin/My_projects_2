import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.107', 5056))
server_socket.listen(2)
print("Сервер запущен. Ожидаем игроков...")


player_1, addr_1 = server_socket.accept()
print(f"Игрок 1 подключен: {addr_1}")

player_2, addr_2 = server_socket.accept()
print(f"Игрок 2 подключен: {addr_2}")

board = [' ' for _ in range(9)]
current_player = 'X'

def format_board():
    return f"""
     {board[0]} | {board[1]} | {board[2]} 
    ---+---+---
     {board[3]} | {board[4]} | {board[5]} 
    ---+---+---
     {board[6]} | {board[7]} | {board[8]} 
    """

def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return None

while True:
    if current_player == 'X':
        player_1.sendall(f"Текущий ход: {current_player}\n{format_board()}\nВыберите позицию (0-8): ".encode())
        player_2.sendall(f"Текущий ход: {current_player}\n{format_board()}\nОжидаем хода игрока 1...".encode())
        move = int(player_1.recv(1024).decode())
        if board[move] == ' ':
            board[move] = current_player
        else:
            player_1.sendall("Эта позиция уже занята, выберите другую!".encode())
            continue
    else:
        player_2.sendall(f"Текущий ход: {current_player}\n{format_board()}\nВыберите позицию (0-8): ".encode())
        player_1.sendall(f"Текущий ход: {current_player}\n{format_board()}\nОжидаем хода игрока 2...".encode())
        move = int(player_2.recv(1024).decode())
        if board[move] == ' ':
            board[move] = current_player
        else:
            player_2.sendall("Эта позиция уже занята, выберите другую!".encode())
            continue

    winner = check_winner()
    if winner:
        if winner == 'X':
            player_1.sendall(f"Поздравляем! Вы победили!\n{format_board()}".encode())
            player_2.sendall(f"К сожалению, вы проиграли.\n{format_board()}".encode())
        else:
            player_2.sendall(f"Поздравляем! Вы победили!\n{format_board()}".encode())
            player_1.sendall(f"К сожалению, вы проиграли.\n{format_board()}".encode())
        break

    current_player = 'O' if current_player == 'X' else 'X'

player_1.close()
player_2.close()
server_socket.close()
