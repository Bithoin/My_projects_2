import socket
import threading
import json

HOST = '192.168.1.107'
PORT = 5054


def load_weather_data():
    try:
        with open('weather.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"города": []}


def handle_client(conn, addr):
    print(f"Подключен {addr}")
    weather_data = load_weather_data()

    try:
        while True:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                break

            try:
                country, city = data.split(',')
                city = city.strip()
                country = country.strip()

                found = False
                for loc in weather_data.get("города", []):
                    if (loc.get("город", "").lower() == city.lower() and
                            loc.get("страна", "").lower() == country.lower()):
                        forecast = "\n".join(
                            f"{day['день']}: {day['температура']}, {day['условия']}"
                            for day in loc.get("погода_на_неделю", [])
                        )
                        response = f"Погода в {city}, {country}:\n{forecast}"
                        found = True
                        break

                if not found:
                    response = f"Данные для {city}, {country} не найдены"

            except Exception as e:
                response = f"Ошибка: {str(e)}"

            conn.send(response.encode('utf-8'))
    finally:
        conn.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Сервер запущен на {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


if __name__ == "__main__":
    main()