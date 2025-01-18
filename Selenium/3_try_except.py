try:
    wiek = int(input('Ile masz lat? '))
except ValueError:
    print('Niepoprawnie wpisany wiek')
    wiek = 0

print(f'Będziesz dorosły za {18 - wiek} lat.')