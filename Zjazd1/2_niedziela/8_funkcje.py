# funkcja, która przyjmuje: wiek, płeć, stan zdrowia
# funkcja zwraca prognozę, jak długo jeszcze
# będzie żył użytkownik

def prognoza(wiek, plec, zdrowie):
    if plec.lower() == 'k':
        result = (90 - wiek) * zdrowie / 100
    elif plec.lower() == 'm':
        result = (77 - wiek) * zdrowie / 100
    else:
        result = 2
    return result


dane = input('Wprowadź wiek, płeć i stan zdrowia:').split()
print(prognoza(int(dane[0]), dane[1], int(dane[2])))