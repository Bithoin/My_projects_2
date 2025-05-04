import socket
import threading
import requests

HOST = '192.168.1.107'
PORT = 5055
API_KEY = 'd974938cde6e89bc06e607ff61f504e0'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city, country):
    try:
        url = f"{BASE_URL}?q={city},{country}&appid={API_KEY}&units=metric&lang=ru"
        response = requests.get(url)

        if response.status_code != 200:
            return f"Ошибка API: {response.json().get('message', 'Неизвестная ошибка')}"

        data = response.json()

        weather_info = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }

        result = (
            f"Погода в {weather_info['city']}, {weather_info['country']}:\n"
            f"Температура: {weather_info['temp']}°C (ощущается как {weather_info['feels_like']}°C)\n"
            f"Описание: {weather_info['description'].capitalize()}\n"
            f"Влажность: {weather_info['humidity']}%\n"
            f"Давление: {weather_info['pressure']} hPa\n"
            f"Скорость ветра: {weather_info['wind_speed']} м/с"
        )

        return result

    except Exception as e:
        return f"Ошибка при получении данных: {str(e)}"


def handle_client(conn, addr):
    print(f"Подключен клиент: {addr}")
    try:
        while True:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                break

            try:
                country, city = data.split(',', 1)
                weather_data = get_weather(city.strip(), country.strip())
                conn.send(weather_data.encode('utf-8'))
            except ValueError:
                conn.send("Неверный формат. Используйте: Страна,Город".encode('utf-8'))
    finally:
        conn.close()
        print(f"Клиент {addr} отключен")


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Сервер запущен на {HOST}:{PORT}")

        try:
            while True:
                conn, addr = s.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
        except KeyboardInterrupt:
            print("Сервер остановлен")


if __name__ == "__main__":
    start_server()