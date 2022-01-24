# File: product.py
# Auth: Kovács Márk Tibor
# Copyright: 2022, Kovács Márk Tibor
# Group: Ifra I N
# Date: 2022-01-04
# https:/github.com/Markuszpolo
# Licenc: GNU GPL

class Product:
    def __init__(self, id=0, name='névtelen', price=0, weight=0):
        self.id = id
        self.name = name
        self.price = int(price)
        self.weight = int(weight)

