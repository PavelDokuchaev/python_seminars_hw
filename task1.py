"""Поработайте с переменными,
# 1 создайте несколько, выведите на экран,
# 2 запросите у пользователя несколько чисел и строк и сохраните в переменные,
 выведите на экран."""

# 1
a = 1
b = 'python'
print(a, b)

# 2
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year_birth = int(input('Введите год рождения: '))
phone_num = int(input('Введите номер телефона: '))
print(f'{name} {surname} \nГода рождения: {year_birth} '
      f'\nНомер телефона: {phone_num}')
