import warnings

def division(x, y):
    if abs(y) < 0.01:
        warnings.warn("Warning: Division by a number close to zero", UserWarning)
    return x / y

warnings.simplefilter("always")
print(division(10, 0.001))


warnings.simplefilter("ignore")
print(division(10, 0.001))


warnings.simplefilter("error")
print(division(10, 0.001))
