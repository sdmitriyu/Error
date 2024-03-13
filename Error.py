def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return ("Ошибка: Невозможно преобразовать строку в число")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except (FileNotFoundError, IOError):
        return ("Ошибка: Файл не найден или произошла ошибка ввода-вывода")

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ("Ошибка: Деление на ноль")
    except TypeError:
        return ("Ошибка: Неверный тип данных для операции деления")


def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return ("Ошибка: Индекс выходит за пределы списка")
    except TypeError:
        return ("Ошибка: Неверный тип данных для доступа к элементу списка")