# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(200, 200)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)

sd.pause()