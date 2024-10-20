
x = input('Wprowadz wartosc: ')
try:
    x = int(x)
    print(f'{x} jest intem')
except:
    try:
        x = float(x)
        print(f'{x} jest floatem')
    except:
        print(f'{x}  zostaje stringiem')