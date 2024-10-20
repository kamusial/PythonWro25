# mamy listę imion
# program ma napisać długość imienia
# i napisać przywitania TYLKO dla mężczyzn

names = ['Przemek', 'Paulina', 'Karolina', 'Adam', 'Iza']
for name in names:
    print(f'Imie {name} ma {len(name)} liter.')
    if name[-1] == 'a':
        continue
    print(f'Witam Pana, Panie {name}')

