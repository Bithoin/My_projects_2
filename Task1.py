# import json
# import pickle
#
# class Auto:
#     def __init__(self, carmodel: str, releaseyear: int, enginevolume: float, carcolor: str, carprice: float):
#         self.carModel = carmodel
#         self.releaseYear = releaseyear
#         self.engineVolume = enginevolume
#         self.carColor = carcolor
#         self.carPrice = carprice
#
#     def output(self):
#         return f"""Модель автомобіля: {self.carModel}
# Рік випуску автомобіля: {self.releaseYear}
# Об'єм двигуна: {self.engineVolume}
# Колір автомобіля: {self.carColor}
# Ціна автомобіля: {self.carPrice} $
# """
#
#     def to_dict(self):
#         return {
#             'carModel': self.carModel,
#             'releaseYear': self.releaseYear,
#             'engineVolume': self.engineVolume,
#             'carColor': self.carColor,
#             'carPrice': self.carPrice
#         }
#
#     @classmethod
#     def create_auto(cls):
#         fields = ["Модель автомобіля", "Рік випуску автомобіля", "Об'єм двигуна", "Колір автомобіля", "Ціна автомобіля"]
#         car_data = []
#         for field in fields:
#             while True:
#                 value = input(f"Введіть {field}: ")
#                 if field == "Рік випуску автомобіля":
#                     try:
#                         value = int(value)
#                         break
#                     except ValueError:
#                         print("Будь ласка, введіть коректний рік (число).")
#                 elif field in ["Об'єм двигуна", "Ціна автомобіля"]:
#                     try:
#                         value = float(value)
#                         break
#                     except ValueError:
#                         print(f"Будь ласка, введіть коректний {field.lower()} (число).")
#                 else:
#                     break
#             car_data.append(value)
#         return cls(car_data[0], car_data[1], car_data[2], car_data[3], car_data[4])
#
# h1 = Auto.create_auto()
#
# auto_dict = h1.to_dict()
#
# json_data = json.dumps(auto_dict)
# print(f"JSON Data: {json_data}")
#
# data_from_json = json.loads(json_data)
# print("Данные после десериализации из JSON:")
# print(data_from_json)
#
# pkl_data = pickle.dumps(auto_dict)
# print(f"Pickle Data: {pkl_data}")
#
# data_from_pkl = pickle.loads(pkl_data)
# print("Данные после десериализации из Pickle:")
# print(data_from_pkl)

# import json
# import pickle
#
# class Book:
#     def __init__(self, title: str, year: int, publisher: str, genre: str, author: str, price: float):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def output(self):
#         return f"""Назва книги: {self.title}
# Рік видання: {self.year}
# Видавець: {self.publisher}
# Жанр: {self.genre}
# Автор: {self.author}
# Ціна: {self.price} грн
# """
#
#     def to_dict(self):
#         return {
#             'title': self.title,
#             'year': self.year,
#             'publisher': self.publisher,
#             'genre': self.genre,
#             'author': self.author,
#             'price': self.price
#         }
#
#     @classmethod
#     def create_book(cls):
#         fields = ["Назва книги", "Рік видання", "Видавець", "Жанр", "Автор", "Ціна"]
#         book_data = []
#         for field in fields:
#             while True:
#                 value = input(f"Введіть {field}: ")
#                 if field == "Рік видання":
#                     try:
#                         value = int(value)
#                         break
#                     except ValueError:
#                         print("Будь ласка, введіть коректний рік (число).")
#                 elif field == "Ціна":
#                     try:
#                         value = float(value)
#                         break
#                     except ValueError:
#                         print("Будь ласка, введіть коректну ціну (число).")
#                 else:
#                     break
#             book_data.append(value)
#         return cls(book_data[0], book_data[1], book_data[2], book_data[3], book_data[4], book_data[5])
#
# book = Book.create_book()
#
# book_dict = book.to_dict()
#
# json_data_book = json.dumps(book_dict)
# print(f"JSON Data (Book): {json_data_book}")
#
# data_from_json_book = json.loads(json_data_book)
# print("Данные после десериализации из JSON (Book):")
# print(data_from_json_book)
#
# pkl_data_book = pickle.dumps(book_dict)
# print(f"Pickle Data (Book): {pkl_data_book}")
#
# data_from_pkl_book = pickle.loads(pkl_data_book)
# print("Данные после десериализации из Pickle (Book):")
# print(data_from_pkl_book)

import json
import pickle

class Stadium:
    def __init__(self, name: str, opening_date: str, country: str, city: str, capacity: int):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def output(self):
        return f"""Назва стадіону: {self.name}
Дата відкриття: {self.opening_date}
Країна: {self.country}
Місто: {self.city}
Вмісткість: {self.capacity} місць
"""

    def to_dict(self):
        return {
            'name': self.name,
            'opening_date': self.opening_date,
            'country': self.country,
            'city': self.city,
            'capacity': self.capacity
        }

    @classmethod
    def create_stadium(cls):
        fields = ["Назва стадіону", "Дата відкриття", "Країна", "Місто", "Вмісткість"]
        stadium_data = []
        for field in fields:
            while True:
                value = input(f"Введіть {field}: ")
                if field == "Вмісткість":
                    try:
                        value = int(value)
                        break
                    except ValueError:
                        print("Будь ласка, введіть коректну вмісткість (число).")
                else:
                    break
            stadium_data.append(value)
        return cls(stadium_data[0], stadium_data[1], stadium_data[2], stadium_data[3], stadium_data[4])

stadium = Stadium.create_stadium()

stadium_dict = stadium.to_dict()

json_data_stadium = json.dumps(stadium_dict)
print(f"JSON Data (Stadium): {json_data_stadium}")

data_from_json_stadium = json.loads(json_data_stadium)
print("Данные после десериализации из JSON (Stadium):")
print(data_from_json_stadium)

pkl_data_stadium = pickle.dumps(stadium_dict)
print(f"Pickle Data (Stadium): {pkl_data_stadium}")

data_from_pkl_stadium = pickle.loads(pkl_data_stadium)
print("Данные после десериализации из Pickle (Stadium):")
print(data_from_pkl_stadium)
