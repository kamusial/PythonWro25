import time


def mierz_czas(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = func(*args, **kwargs)
        koniec = time.time()
        print(f"Czas wykonania {func.__name__}: {koniec - start:.4f} sekundy")
        return wynik
    return wrapper

@mierz_czas
def wez_policz(n):
    suma = 1
    for i in range(n):
        suma += i
    return suma

@mierz_czas
def dzielenie(a, b):
    for _ in range(1000000):
        x = a / b
    return x

wynik = wez_policz(1000000)
print(f'Wynik wynosi: {wynik}')

print(dzielenie(100.453, 3.67))
