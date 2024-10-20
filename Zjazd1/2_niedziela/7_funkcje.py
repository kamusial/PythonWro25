def welcome(name):
    if name[-1] == 'a':
        print('Witam Panią')
    print(f'Witaj {name}')
    print(f'Trwa zakładanie maila {name}@wsb.pl')
    print('Zgłoś się do recepcji')


def BMI(wzrost, waga):
    result = waga / (wzrost**2)
    return round(result, 2)



waga = int(input('Podaj wage w kilogramach: '))
wzrost = float(input('Podaj wzrost w m: '))
print(BMI(wzrost, waga))


