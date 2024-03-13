class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def generate_exception(data):
    if data < 0:
        raise InvalidDataException("Invalid data: {}".format(data))
    elif data == 0:
        raise ProcessingException("Processing exception: {}".format(data))
    else:
        print("Data is valid: {}".format(data))


def caller_function(data):
    try:
        generate_exception(data)
    except InvalidDataException as e:
        print("Caught InvalidDataException:", e)
        raise  # Передача исключения дальше по стеку вызовов
    except ProcessingException as e:
        print("Caught ProcessingException:", e)
        raise  # Передача исключения дальше по стеку вызовов


# Вызов функций и обработка исключений
try:
    caller_function(-5)
except InvalidDataException as e:
    print("Caught InvalidDataException in caller_function:", e)
except ProcessingException as e:
    print("Caught ProcessingException in caller_function:", e)
