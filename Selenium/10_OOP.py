class Auto:
    def __init__(self, kolor, stan, rocznik=2000):
        self.kolor = kolor
        self.przebieg = 0
        self.stan = stan
        self.ilosc_paliwa = 5
        self.zarezerwowane = False
        self.wiek = 2025 - rocznik


auto1 = Auto('white', 3, 1999)


