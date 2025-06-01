NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma = zbior1 | zbior2
# przeciecie = zbior1 & zbior2
# roznica = zbior1 - zbior2
# roznica_symetryczna = zbior1 ^ zbior2

# sprawdźmy, ile osób chorowało w ostatnim roku na krzykach
print(f'\nChorzy w ostatnim roku na krzykach: {chorzy_rok & krzyki}')
print(f'ilość: {len(chorzy_rok & krzyki)}')

# sprawdźmy ile osób z Krzyków chorowało w ostatnim roku
print(f'\nChorzy w ostatnim roku na krzykach: {krzyki & chorzy_rok}')
print(f'ilość: {len(krzyki & chorzy_miesiac)}')

# sprawdźmy, ile osób chorowało w ostatnim miesiącu w centrum
print(f'\nChorzy w ostatnim miesiącu w centrum {centrum & chorzy_miesiac}')
print(f'Ilość {len(centrum & chorzy_miesiac)}')

# sprawdźmy, ile osób mieszka w sumie w centrum i na krzykach
print(f'\nMieszkańcy centrum i krzyków: {krzyki | centrum}')
print(f'Ilosc {len(krzyki | centrum)}')

# sprawdźmy poprawność danych:
print('\nPoprawność danych')

# każdy, kto chorował w ostatnim miesiącu,
# jednocześnie chorował w ostatnim roku
print(f'\nLudzie chorujący w ostatnim miesiącu i NIE chorujący w ostatnim roku {chorzy_miesiac - chorzy_rok}')
print(f'Ilosc {len(chorzy_miesiac - chorzy_rok)}')
if len(chorzy_miesiac - chorzy_rok) == 0:
    print('ok')

# nikt nie powinien mieszkać jendocześnie w centrum i na krzykach
# – jeśli tak, trzeba usunąć
# zbior.remove(element)

if len(krzyki.intersection(centrum)) != 0:
    x = input('Usinąć z centrum (C), czy z krzyków (K)? ')
    duplikaty = krzyki.intersection(centrum)
    if x.lower() == 'k':
        krzyki = krzyki.difference(duplikaty)
    elif x.lower() == 'c':
        for pesel in duplikaty:
            centrum.remove(pesel)
    else:
        print('zly wybor')
    print('Sprawdzam duplikaty: ',krzyki.intersection(centrum))

# każdy: chory, zdrowy, z krzyków i z centrum, powinien być w bazie NFZ.
# Jeśli nie ma, trzeba dopisać

# lista = [1, 2, 3, 3, 3, 4, 4, 4, 5]
# lista = list(set(lista))
# print(lista)
pozaNFZ = chorzy_rok.union(chorzy_miesiac.union(krzyki.union(centrum))).difference(NFZ)
if len(pozaNFZ) != 0:
    print(pozaNFZ)
    NFZ = NFZ.union(pozaNFZ)

# każdy: chory, zdrowy, z centeum i z krzyków, powinien być w bazie NFZ. Jeśli nie ma, trzeba dopisać)
wszyscy = chorzy_rok | chorzy_miesiac | centrum | krzyki
NFZ |= wszyscy
print(len(NFZ))

# pesele żeńskie mają ostatnią cyfrę parzystą, męskie – nieparzystą.
# zróbmy nowe zbiory, osobne dla mężczyzn i kobiet
NFZ_men = set()
NFZ_women = set()
for pesel in NFZ:
    if pesel % 2 == 0:
        NFZ_women.add(pesel)
NFZ_men = NFZ - NFZ_women