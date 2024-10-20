x = int(input('Ile razy chcesz wykonac kod?   '))

while x > 0:
    print('Lecimy')
    x = x - 1
    print('x wynosi',x)
print('koniec programu')

passwd = input('Podaj haslo:   ')
while passwd != 'Piesek':
    print('Złe hasło')
    passwd = input('Jeszcze raz:   ')
print('Witamy w programie')


# program pyta o liczbę dni urlopu, któe pracownik chce wykorzytać
# program przyjmuje liczby od 1 do 99

urlop = int(input('Ile urlopu chcesz wykorzystać?  '))
while urlop < 1 or urlop > 99:
    print('Zła wartość, jeszcze raz')
    urlop = int(input('Ile urlopu chcesz wykorzystać?  '))
print('Obliczam urlop')


# pracownik wpisuje ile ma dni urlopu
# program pyta o liczbę dni urlopu, któe pracownik chce wykorzytać
# program przyjmuje liczby od 1 do dostepnych dni urlopu

dostepny_urlop = int(input('Ile masz urlopu?   ')
urlop = int(input('Ile urlopu chcesz wykorzystać?  '))
while urlop < 1 or urlop > dostepny_urlop:
    print('Zła wartość, jeszcze raz')
    urlop = int(input('Ile urlopu chcesz wykorzystać?  '))
print('Obliczam urlop')
print('Zostało',dostepny_urlop - urlop,'dni')



