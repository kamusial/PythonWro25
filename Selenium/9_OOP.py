class Employee:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.id = 1234
        self.holiday = 26


    def take_holiday(self, days):
        if days > 0 and days <= self.holiday:
            self.holiday -= days
        else:
            print('Niepoprwane dane, brak zmian')

    def add_holiday(self, days):
        if days > 0:
            passwd = input('Wprowadz hasło')
            if passwd == 'admin1':
                print(f'Dodano {days} dni urlopu ')
                print(f'Wysłano miala do pracownika {self.id}')
                self.holiday += days
            else:
                print('brak dostę[pu')


emp1 = Employee()
print(emp1.imie)
emp1.nazwisko = 'Zakoscielny'
print(emp1.nazwisko)

napis = 'mama'
print(type(napis))
emp2 = Employee()

emp1.add_holiday(6)
print(emp1.holiday)

emp2.take_holiday(30)