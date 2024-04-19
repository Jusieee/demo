# -*- coding: utf-8 -*-

my_family = ['Мама','Папа','Сестра','Брат']
my_family_height = [
     ['Елена', 160],
     ['Александр', 195],
     ['Алина', 167],
     ['Даниил', 150],
]

print(my_family[1], "-", my_family_height[1][1], "см")

Rost = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]

print('Общий рост моей семьи -', Rost, 'см')