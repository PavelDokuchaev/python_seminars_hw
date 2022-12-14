"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться
на русские. Новый блок строк должен записываться в новый текстовый файл."""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('numbers.txt', 'r') as f_obj:
    for line in f_obj:
        line = line.split(' ', 1)
        new_file.append(rus[line[0]] + ' ' + line[1])
    print(new_file)
with open('numbers_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
