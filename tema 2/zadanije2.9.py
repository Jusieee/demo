# -*- coding= utf-8 -*-

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

all_flower = garden_set | meadow_set

print(all_flower)

other_flower = garden_set & meadow_set

print(other_flower)

garden_inclusive = garden_set - meadow_set

print(garden_inclusive)

meadow_inclusive = meadow_set - garden_set

print(meadow_inclusive)