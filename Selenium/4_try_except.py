try:
    liczba_punktow = int(input('ile masz punktow? '))
    wiek = int(input('Ile masz lat? '))
    poziom = liczba_punktow / wiek
    imie = input('Jak sie nazywasz? ')
    print(imie[6])
    with open('dane') as file:
        file.read()

except ValueError:
    print('Niepoprawnie wpisany wiek')
    wiek = 100
except ZeroDivisionError:
    print('Wiek nie moze byc zerem. Zakladam poziom 0')
    poziom = 0
except FileNotFoundError:
    print('Nie ma takiego pliku')
except IndexError:
    print('Za krotkie imie? ')

print(f'Będziesz dorosły za {18 - wiek} lat.')