# -*- coding: utf-8 -*-

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

x = month

if x == 2:
    print(28)
elif x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print(31)
elif x == 4 or x == 6 or x == 9 or x == 11:
    print(30)
else:
    print('номер месяца некорректен')