print('Witamy w panelu logowania')

while True:
    user = input('Wprowadź nazwe użytkownika:   ')
    passwd = input('Wprowadź hasło:   ')
    if user == 'Kamil' and passwd == 'Piesek':
        print('Poprawne dane, witaj',user)
        break
    elif passwd == 'serwis':
        print('Wprowadziłś hasło serwisowe')
        break
    else:
        print('Niepoprawne dane logowania, jeszcze raz')
print('użtkownik zalogowany')
