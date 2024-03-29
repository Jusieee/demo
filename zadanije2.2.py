# -*- coding: utf-8 -*-

from pprint import pprint

radius = 42
Pi = 3.1415926

S = Pi * ((radius)**2)

pprint(round(S, ndigits=4))

point = (23, 34)
d1 = (((point[0])*2+(point[1])*2)**.5)

pprint(radius > d1)


