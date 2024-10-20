zarobki = float(input('Ile zarabiasz?   '))

if zarobki > 5000:
    print('Podatek 20%, na rękę',zarobki * 0.8)
    print('Jesteś bogady')
elif zarobki > 3000:
    print('Podatek 10%, na rękę',zarobki * 0.9)
    print('Niski podatek')
elif zarobki > 0:
    print('Podatek 0%, na rękę',zarobki)
    print('Zwolniony z podatku')
elif zarobki == 0:
    print('Nie zarabiasz, nie ma podatku')
else:
    print('niepoprawna kwota')
print('dalsza czesc programu')


