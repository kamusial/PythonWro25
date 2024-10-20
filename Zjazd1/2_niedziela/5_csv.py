#1. Odczyt csv z zapisem poszczególnych pól

# with open('rozliczenie.csv', 'r') as file1:
path = 'rozliczenie.csv'
mode = 'r'
with open(path, mode) as file_csv:
    content = file_csv.readlines()
print(content)
print(content[4])
for i in range(len(content)):
    print(f'przed: {content[i]}')
    content[i] = content[i].split(';')
    print(f'po: {content[i]}')
print(content)    # wszystko
print(content[3]) # jeden wiersz
print(content[3][2])   # jedna komórka
print('Koniec części 1\n')

#2. Obliczanie średniej wypłaty
# for i in range(1,len(content)):
#     print(content[i][1])
total = 0
for line in content[1:]:
    total += int(line[1])
print(f'Średnia wypłata {total / (len(content)-1)}')
print('Koniec części 2\n')

#3. Ile kobiet jest na macierzynskim?
total = 0
for line in content[1:]:
    line[4] = line[4].replace('\n','')
    if line[4].lower() == 't' and line[3].lower() == 'k':
        total += 1
print(f'{total} kobiety na macierzynskim')