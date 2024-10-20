sample = 'Konstantynopol'
print(sample[9:2:-1])     #  od, do, krok

word = input('Wprowadz slowo: ')
word = word.lower()
if word == word[::-1]:  # słowo od końac
    print('To jest anagram')