# program losuje liczb / ma liczbę
# użytkownik zgaduje liczbę, a program pisze, czy zgadywana liczba jest większa, mniejsza, czy równa
import random
a = int(input(' OD jakiej liczby losujemy?   '))
b = int(input(' DO jakiej liczby losujemy?   '))
liczba = random.randint(a, b)
print('Wylosowałem liczbę z przedziału',a,',',b)
licznik = 0
while True:
    if licznik == 3:
        print('Przekroczono liczbe prób')
        break
    liczba_uzytkownika = int(input('Zgadnij liczbę:   '))
    if liczba_uzytkownika > liczba:
        print('za dużo')
    elif liczba_uzytkownika < liczba:
        print('za mało')
    else:
        print('Zgadłeś')
        break
    licznik += 1
