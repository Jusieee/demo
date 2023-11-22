# -*- coding: utf-8 -*-

from pprint import pprint

sites = {
    'Mos': (550, 370),
    'Lon': (510, 510),
    'Par': (480, 480),
}

distances = {}

Moscow = sites['Mos']
London = sites['Lon']
Paris = sites['Par']

MosLon = ((Moscow[0] - London[0])**2 + (Moscow[1] - London[1])**2)
MosPar = ((Moscow[0] - Paris[0])**2 + (Moscow[1] - Paris[1])**2)
LonPar = ((London[0] - Paris[0])**2 + (London[1] - Paris[1])**2)

distances['Москва'] = {}
distances['Москва']['Лондон'] = MosLon
distances['Москва']['Париж'] = MosPar

distances['Лондон'] = {}
distances['Лондон']['Москва'] = MosLon
distances['Лондон']['Париж'] = LonPar

distances['Париж'] = {}
distances['Париж']['Москва'] = MosPar
distances['Париж']['Лондон'] = LonPar

pprint(distances)