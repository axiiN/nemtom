


zoldsegnev = ''
elfogadott = ['karalábé', 'vöröshagyma', 'cékla', 'paprika']
darab = 0
while zoldsegnev != 'vege':
    zoldsegnev = input('Zölségnév: ')
    if zoldsegnev in elfogadott:
        darab += 1
        print('Ok')
    else:
        print('Nem megfelelő zöldség')

print('Elfogadott zöldségek:', darab)

