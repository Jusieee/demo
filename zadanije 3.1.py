# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(200, 200)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)

def bubble(point, step):
    radius = step
    sd.circle(center_position=point, radius=radius)

point = sd.get_point(500, 500)
bubble(point=point, step=20)

for x in range(50, 510, 50):
    point = sd.get_point(x, 500)
    bubble(point=point, step=5)

for x in range(40, 401, 40):
    for y in range(40, 120, 30):
        point = sd.get_point(x, y)
        bubble(point=point, step=10)

for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=100)

sd.pause()