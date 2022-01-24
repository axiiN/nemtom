

zoldsegnev = input('Zöldségnév: ')

if zoldsegnev == '':
    print('Nem adtál meg zöldségget')
    exit()

zoldsegek = ['cékla', 'vöröshagyma', 'karalábé']
if zoldsegnev in zoldsegek:
    print('Rendben')
else:
    print('Nincs ilyen zöldség')


