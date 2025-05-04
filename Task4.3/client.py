import socket

HOST = '192.168.1.107'
PORT = 5055


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"Подключено к серверу {HOST}:{PORT}")

            while True:
                print("\nВведите запрос:")
                country = input("Страна (например: Ukraine): ").strip()
                city = input("Город (например: Kyiv): ").strip()

                if not country or not city:
                    print("Оба поля обязательны!")
                    continue

                s.sendall(f"{country},{city}".encode('utf-8'))
                data = s.recv(4096).decode('utf-8')
                print("\n" + data + "\n")

                if input("Продолжить? (y/n): ").lower() != 'y':
                    break

        except ConnectionRefusedError:
            print("Не удалось подключиться к серверу")
        except Exception as e:
            print(f"Ошибка: {str(e)}")
        finally:
            print("Соединение закрыто")


if __name__ == "__main__":
    main()