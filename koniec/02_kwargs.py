def wpisz_dane(x, y, *punkty, **czlowiek):
    print(f'Wspolrzedne to: {x} i {y}')
    punkty_suma = 0
    for punkt in punkty:
        if punkt > 0:
            punkty_suma += punkt
    if czlowiek['wiek'] >= 18:
        print(f"hej {czlowiek['imie']} z {czlowiek['miasto']}")


wpisz_dane(155, 43, 4, 3, 23, 12, imie='Kamil', wiek=18, miasto='Wroclaw')

