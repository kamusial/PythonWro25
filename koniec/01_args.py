def sum(*liczby):
    wynik = 0
    for liczba in liczby:
        wynik += liczba
    return wynik


kalorycznosc = \
    {'marchew': 20, 'chipsy': 500, 'cola_zero': 0, 'chleb': 75}

def bilans_kaloryczny(tryb_zycia, *produkty):
    kalorie = 0
    for produkt in produkty:
        if produkt in kalorycznosc.keys():
            kalorie += kalorycznosc[produkt]
        else:
            print('Nie znaleziono produktu')
            return None
    if kalorie > 3000 and tryb_zycia < 5:
        return 'Jesz za duzo'
    return 'Jesz ok'


