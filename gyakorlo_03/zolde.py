# File: zolde.py
# Auth: Kovács Márk Tibor
# Copyright: 2022, Kovács Márk Tibor
# Group: Ifra I N
# Date: 2022-01-04
# https:/github.com/Markuszpolo
# Licenc: GNU GPL

def jo_zoldseg(nev):
    zoldsegek = ["cékla", "vöröshagyma", "karalábé"]
    if nev in zoldsegek:
        return True
    else:
        return False

darab_jo = 0
nev = ""
while nev != "vege":
    nev = input("Zöldség neve: ")
    if nev != "vege":
        if jo_zoldseg(nev):
            print("Oké")
            darab_jo += 1
        else:
            print("Nem megfelelő zöldség")
print("Jó zöldségek darab száma:", darab_jo)