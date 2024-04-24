# -*- coding: utf-8 -*-

educational_grant, expenses = 10000, 12000

i = 1
e_g_all = 0
exp_all = 0

while i <= 10:
    e_g_all += educational_grant
    exp_all += expenses * 1.03
    i += 1

money = exp_all - e_g_all
print('Студенту надо попрочить', money, 'рублей')