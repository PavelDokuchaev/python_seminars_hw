"""Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить возведение числа x
в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора возведения в степень.
Второй — более сложная реализация без оператора возведения в степень,
предусматривающая использование цикла."""

"""Первый — возведение в степень с помощью оператора возведения в степень."""


def my_func_1(x, y):
    return x ** abs(y)


print(my_func_1(int(input('Введите действительное положительное число: ')),
                int(input('Введите целое отрицательное число: '))))

"""Второй — более сложная реализация без оператора возведения в степень,
предусматривающая использование цикла."""


def my_func_2(x, y):
    res = 1
    y = abs(y)
    while 0 < y:
        res = res * x
        y -= 1
    return res


print(my_func_2(int(input('Введите действительное положительное число: ')),
                int(input('Введите целое отрицательное число: '))))