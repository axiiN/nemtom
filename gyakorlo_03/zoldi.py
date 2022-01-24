# File: zoldi.py
# Auth: Kovács Márk Tibor
# Copyright: 2022, Kovács Márk Tibor
# Group: Ifra I N
# Date: 2022-01-04
# https:/github.com/Markuszpolo
# Licenc: GNU GPL

zoldseg_nev = input("Zöldség neve: ")
if zoldseg_nev == "":
    exit()

zoldsegek = ["cékla", "vöröshagyma", "karalábé"]
if zoldseg_nev in zoldsegek:
    print("Rendben")
else:
    print("Nincs ilyen zöldség")