# -*- coding= utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price

table_code = goods['Стол']
tables_item = store[table_code][0]
tables_item_1 = store[table_code][1]
tables_quantity = tables_item['quantity']
tables_price = tables_item['price']
tables_quantity_1 = tables_item_1['quantity']
tables_price_1 = tables_item_1['price']
tables_cost = tables_quantity * tables_price + tables_quantity_1 * tables_price_1
tables_quantity = tables_quantity + tables_quantity_1

print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб',
      'Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')