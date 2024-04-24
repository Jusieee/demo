# -*- coding: utf-8 -*-

a: int
a, b = 179, 37
x = 0
while a > b:
    x += 1
    a -= b

print('Целочисленное деление', a, 'на', b, 'дает', x)