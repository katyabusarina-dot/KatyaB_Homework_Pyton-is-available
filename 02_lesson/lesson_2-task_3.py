import math


def square(x):
    return math.ceil(x**2)


x = float(input("Введите сторону квадата:"))
print(f'Округленная в большую сторону сумма - {square(x)}')
