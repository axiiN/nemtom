# File: grower.py
# Auth: Kovács Márk Tibor
# Copyright: 2022, Kovács Márk Tibor
# Group: Ifra I N
# Date: 2022-01-04
# https:/github.com/Markuszpolo
# Licenc: GNU GPL

from product import Product
class Grower:
    def read_file(self):
        fp = open('products.txt', 'r', encoding="utf-8")
        lines = fp.readlines()
        fp.close()

        self.products = []

        for line in lines[1::]:
            (id, name, price, quantity) = line.split(';')
            product = Product(id, name, price, quantity)
            self.products.append(product)
    
    # legdrágább zöldség
    def larger(self):
        max_product = self.products[0]
        for product in self.products:
            if product.price > max_product.price:
                max_product = product
        print("Legdrágább zöldség: ", max_product.name, max_product.price)
    
    # Az összes paprika ára
    def calcPepperPrice(self):
        ossz_ar = 0
        for product in self.products:
            if product.name == "paprika":
                ossz_ar = product.price * product.weight
        print("Paprika készleten ár alapján: ", ossz_ar)
            

    # Mennyi a vöröshagyma és a karalábé tömege együtt?
    def sumOnionKohlrabiWeight(self):
        ossz_tomeg = 0
        for product in self.products:
            if product.name == "vöröshagyma" or product.name == "karalábé":
                ossz_tomeg += product.weight
        print("Hagyma és karalábé össz tömege: ", ossz_tomeg)
    
    # Mi a neve legnagyobb tömegű zöldségnek?
    def showLargerWeight(self):
        max_product = self.products[0]
        for product in self.products:
            if product.weight > max_product.weight:
                max_product = product
        print("Legnagyobb tömegű zöldség: ", max_product.name, max_product.weight)
    
    # Van karalábé?
    def isHaveKohlrabi(self):
        n = len(self.products)
        zoldi = "karalábé"
        i = 0
        while i < n and self.products[i].name.find(zoldi) == -1:
            i += 1
        if i < n:
            print("Van ilyen")
        else:
            print("Nincs ilyen")

    # Hány zöldség drágább mint 700 Ft.
    def moreThenSevenhundred(self):
        darab = 0
        for product in self.products:
            if product.price > 700:
                darab += 1
        print("Hány darab zöldség drágább mint 700?:", darab)
        
grower = Grower()
grower.read_file()
grower.larger()
grower.calcPepperPrice()
grower.sumOnionKohlrabiWeight()
grower.showLargerWeight()
grower.isHaveKohlrabi()
grower.moreThenSevenhundred()