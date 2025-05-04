import socket

HOST = '192.168.1.107'
PORT = 5054


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Подключено к {HOST}:{PORT}")

        while True:
            print("\nВведите данные для запроса:")
            country = input("Страна: ").strip()
            city = input("Город: ").strip()

            if not country or not city:
                print("Оба поля обязательны!")
                continue

            s.sendall(f"{country},{city}".encode('utf-8'))
            data = s.recv(4096).decode('utf-8')
            print("\nРезультат:")
            print(data)

            if input("\nПродолжить? (y/n): ").lower() != 'y':
                break


if __name__ == "__main__":
    main()