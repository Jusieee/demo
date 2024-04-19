# -*- coding: utf-8 -*-

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

zoo.insert(1, 'bear')

print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]

zoo = zoo + birds

print(zoo)

zoo.remove('elephant')

print(zoo)

print('Лев находится в клетке номер -', zoo.index('lion'))
print('Жаворонок находится в клетке номер -', zoo.index('lark'))
