"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict"""

list_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input('Введите номер месяца: '))
if month == 12 or month == 1 or month == 2:
    print(f'Этот месяц относится к времени года - {list_seasons[0]}')
elif month == 3 or month == 4 or month == 5:
    print(f'Этот месяц относится к времени года - {list_seasons[1]}')
elif month == 6 or month == 7 or month == 8:
    print(f'Этот месяц относится к времени года - {list_seasons[2]}')
elif month == 9 or month == 10 or month == 11:
    print(f'Этот месяц относится к времени года - {list_seasons[3]}')
else:
    print('Такого месяца не существует')

dict_seasons = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна',
                5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
                10: 'Осень', 11: 'Осень'}
month = int(input('Введите номер месяца: '))
if month < 1 or month > 12:
    print('Такого месяца не существует')
else:
    print(f'Этот месяц относится к времени года - {dict_seasons[month]}')



