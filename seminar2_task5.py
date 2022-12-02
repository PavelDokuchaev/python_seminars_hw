"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
my_list = [7, 5, 3, 3, 2]."""

my_list = [7, 5, 3, 3, 2]
user_digit = int(input('Введите число: '))
print(f'Исходный рейтинг: {my_list}')
for el in range(len(my_list)):
    if user_digit == my_list[el]:
        my_list.insert(el + 1, user_digit)
        break
    elif user_digit < my_list[el]:
        my_list.append(user_digit)
        break
    elif user_digit > my_list[el]:
        my_list.insert(0, user_digit)
        break
print(f'Обновленный рейтинг: {my_list}')



