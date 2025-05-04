# import multiprocessing
#
# def max_in_list(value_list):
#     max_value = max(value_list)
#     print(f"Максимальне значення: {max_value}")
#
# def min_in_list(value_list):
#     min_value = min(value_list)
#     print(f"Мінімальне значення: {min_value}")
#
#
# if __name__ == "__main__":
#     user_input = input("Введіть числа через пробіл: ")
#     value_list = list(map(int, user_input.split()))
#
#     process1 = multiprocessing.Process(target=max_in_list, args=(value_list,))
#     process2 = multiprocessing.Process(target=min_in_list, args=(value_list,))
#
#     process1.start()
#     process2.start()
#
#     process1.join()
#     process2.join()

# import multiprocessing
#
# def max_in_list(value_list):
#     sum_value = sum(value_list)
#     print(f"Сума чисел: {sum_value}")
#
# def min_in_list(value_list):
#     mean_value = sum(value_list) / len(value_list)
#     print(f"Середнє арифметичне: {mean_value}")
#
#
# if __name__ == "__main__":
#     user_input = input("Введіть числа через пробіл: ")
#     value_list = list(map(int, user_input.split()))
#
#     process1 = multiprocessing.Process(target=max_in_list, args=(value_list,))
#     process2 = multiprocessing.Process(target=min_in_list, args=(value_list,))
#
#     process1.start()
#     process2.start()
#
#     process1.join()
#     process2.join()


import multiprocessing



def write_even_numbers(numbers, filename):
    even_numbers = [num for num in numbers if num % 2 == 0]
    with open(filename, 'w') as f:
        for num in even_numbers:
            f.write(f"{num}\n")
    print(f"Кількість парних чисел: {len(even_numbers)}")


def write_odd_numbers(numbers, filename):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    with open(filename, 'w') as f:
        for num in odd_numbers:
            f.write(f"{num}\n")
    print(f"Кількість непарних чисел: {len(odd_numbers)}")


def main():
    file_path = input("Введіть шлях до файлу, що містить числа: ")

    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        even_process = multiprocessing.Process(target=write_even_numbers, args=(numbers, 'Files/even_numbers.txt'))
        odd_process = multiprocessing.Process(target=write_odd_numbers, args=(numbers, 'Files/odd_numbers.txt'))

        even_process.start()
        odd_process.start()

        even_process.join()
        odd_process.join()

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях.")
    except ValueError:
        print("У файлі повинні бути лише числа.")


if __name__ == '__main__':
    main()


# import multiprocessing
#
# def search_word_in_file(file_path, search_word, result_queue):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
#             count = content.lower().count(search_word.lower())
#             result_queue.put(count)
#     except FileNotFoundError:
#         result_queue.put("Файл не знайдено.")
#     except Exception as e:
#         result_queue.put(str(e))
#
# def main():
#     file_path = input("Введіть шлях до файлу: ")
#     search_word = input("Введіть слово для пошуку: ")
#
#     result_queue = multiprocessing.Queue()
#
#     search_process = multiprocessing.Process(target=search_word_in_file, args=(file_path, search_word, result_queue))
#     search_process.start()
#
#     search_process.join()
#
#     result = result_queue.get()
#
#     if isinstance(result, int):
#         print(f"Слово '{search_word}' зустрічається {result} раз(ів) у файлі.")
#     else:
#         print(result)
#
# if __name__ == '__main__':
#     main()
#




