import threading
import random

# List = []
#
# def fill_list():
#     global List
#     for _ in range(100):
#         List.append(random.randint(1, 100))
#
# def sum_list():
#     print(f"Сумма: {sum(List)}")
#
# def arithmetic_mean():
#     print(f"Среднее арифметическое: {sum(List) / len(List)}")
#
# thread_fill = threading.Thread(target=fill_list, name="Fill")
#
# thread_fill.start()
# thread_fill.join()
#
# thread_sum = threading.Thread(target=sum_list, name="Sum")
# thread_mean = threading.Thread(target=arithmetic_mean, name="Mean")
#
# thread_sum.start()
# thread_mean.start()
#
# thread_sum.join()
# thread_mean.join()

# Користувач вводить з клавіатури шлях до файлу. Після чого запускаються три потоки.
# Перший потік заповнює файл випадковими числами.
# Два інші потоки очікують на заповнення.
# Коли файл заповнений, обидва потоки стартують.
# Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі.
# Результати пошуку кожен потік має  записати у новий файл.
# Виведіть на екран статистику виконаних операцій.

# import os
#
# current_directory = os.path.dirname(os.path.abspath(__file__))
# file_name = input("Введите имя файла: ")
# file_path1 = os.path.join(current_directory, file_name)
#
# def fill_file():
#     global file_path1
#     with open(file_path1, "w") as f:
#         for _ in range(0, 100):
#             f.write(f"{random.randint(1, 10)}\n")
#
# def find_simple_numbers():
#     global file_path1
#     global current_directory
#     with open(file_path1, "r") as f:
#         simple_numbers = []
#         for line in f:
#             number = int(line.strip())
#             if all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
#                 simple_numbers.append(number)
#     file_path2 = os.path.join(current_directory, "file_with_simple_numbers")
#     with open(file_path2, "w") as f:
#         f.write("\n".join(map(str, simple_numbers)))
#     print(simple_numbers)
#
# def find_factorial_numbers():
#     global file_path1
#     global current_directory
#     with open(file_path1, "r") as f:
#         factorial_numbers = []
#         for line in f:
#             number = int(line.strip())
#             factorial = 1
#             for i in range(1, number + 1):
#                 factorial *= i
#             factorial_numbers.append(factorial)
#     file_path3 = os.path.join(current_directory, "file_with_factorial_numbers")
#     with open(file_path3, "w") as f:
#         f.write("\n".join(map(str, factorial_numbers)))
#     print(factorial_numbers)
#
# thread_fill = threading.Thread(target=fill_file, name="Fill")
# thread_fill.start()
# thread_fill.join()
#
# thread_simple_numbers = threading.Thread(target=find_simple_numbers, name="simple_numbers")
# thread_factorial_numbers = threading.Thread(target=find_factorial_numbers, name="factorial_numbers")
#
# thread_simple_numbers.start()
# thread_factorial_numbers.start()
#
# thread_simple_numbers.join()
# thread_factorial_numbers.join()

# import os
# import shutil
# import threading
#
# def copy_directory(src, dst):
#     if not os.path.exists(dst):
#         os.makedirs(dst)
#     for item in os.listdir(src):
#         s = os.path.join(src, item)
#         d = os.path.join(dst, item)
#         if os.path.isdir(s):
#             copy_directory(s, d)
#         else:
#             shutil.copy2(s, d)
#     print(f"Копирование из {src} в {dst} завершено.")
#
# src_dir = input("Введите путь к существующей директории: ")
# dst_dir = input("Введите путь к новой директории: ")
#
# thread_copy = threading.Thread(target=copy_directory, args=(src_dir, dst_dir), name="CopyDirectory")
# thread_copy.start()
# thread_copy.join()
#
# print("Операция копирования завершена.")
#
import os
import threading


def find_files_with_word(directory, word, output_file):
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as infile:
                    for line in infile:
                        if word in line:
                            outfile.write(line)
    print(f"Файлы с словом '{word}' объединены в {output_file}")


def remove_forbidden_words(input_file, forbidden_words_file, output_file):
    with open(forbidden_words_file, 'r') as f:
        forbidden_words = set(word.strip() for word in f)

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            for word in forbidden_words:
                line = line.replace(word, '')
            outfile.write(line)
    print(f"Запрещенные слова удалены из {input_file} и результат записан в {output_file}")


directory = input("Введите путь к существующей директории: ")
search_word = input("Введите слово для поиска: ")
forbidden_words_file = input("Введите путь к файлу с запрещенными словами: ")

intermediate_file = "intermediate_file.txt"
final_output_file = "final_output_file.txt"

thread_find = threading.Thread(target=find_files_with_word, args=(directory, search_word, intermediate_file),
                               name="FindFiles")
thread_find.start()
thread_find.join()

thread_remove = threading.Thread(target=remove_forbidden_words,
                                 args=(intermediate_file, forbidden_words_file, final_output_file),
                                 name="RemoveForbiddenWords")
thread_remove.start()
thread_remove.join()

print("Операции завершены.")
