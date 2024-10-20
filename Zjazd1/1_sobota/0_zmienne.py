print('siema')

a = 5
b = 7.5
c = 'piesek'

print(type(a))
print(type(b))
print(type(c))

print(a + b)
# print(a + c)
print(a * c)
# print(b * c)
d = 'kotek'
print(c + d)
wynik = (a + b) * 3
print('Wynik rownania to')
print(wynik)
print('Wynik to',wynik,'i juz')

x = input('Ile masz zwierząt?   ')
print('Więc mówisz że masz',x,'zwierząt')



'''
wiek = input('Ile masz lat?   ')
print('masz',wiek,'lat')
wiek_int = int(wiek)
print('Będziesz pełnoletni za',18-wiek_int,'lat')
'''

# program, który pyta o liczbę dzieci i zarobki
# progrma liczy kwotę na osobę w rodzinie

liczba_dzieci = int(input('Ile masz dzieci? '))
zarobki = float(input('Ile zarabiasz?  '))
kasa_w_rodzinie = liczba_dzieci * 800 + zarobki
kasa_na_glowe = kasa_w_rodzinie /(liczba_dzieci + 2)
kasa_zaokraglona = round(kasa_na_glowe, 2)
print('Na głowę w rodzinie jest',kasa_zaokraglona)

print('Kasa na glowe', round((liczba_dzieci * 800 + zarobki)/(liczba_dzieci+2),2))





