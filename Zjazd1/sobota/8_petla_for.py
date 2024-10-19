for i in range(5):
    print('powtorzenie',i+1,'wartość iteratora',i)

slowo = input('Wpisz slowo:  ')
licznik = 0
for i in range(len(slowo)):
    print(slowo[i])
    if slowo[i] == 'a':
        print('znaleziono literę "a"')
        licznik += 1
print('Litera a występuje ',licznik,'razy')
licznik = 0
lista_zakupow = ['marchew', 'sok', 'kefir', 'olej']
for i in range (len(lista_zakupow)):
    print(i+1,'słowo to',lista_zakupow[i],'. Słowo ma',len(lista_zakupow[i]),'liter')
#    print(f'{i+1} słowo to {lista_zakupow[i]}. Słowo ma {len(lista_zakupow[i])} liter')
    if len(lista_zakupow[i]) > 4:
#        lista_zakupow[i] = '########'
        licznik += 1
print('lista długich słów:',licznik)


