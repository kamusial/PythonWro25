def silnia1(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik
print(f'silnia z 5 to: {silnia1(5)}')

def silnia2(n):
    if n == 1:
        print(f'{n} = ', end='')
        return 1
    else:
        print(f'{n} * ', end='')
        return n * silnia2(n-1)

print(silnia2(5))
