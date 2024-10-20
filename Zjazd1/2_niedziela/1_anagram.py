word = input('Wprowadz slowo: ')

no_of_reps = len(word) // 2  # część całkowita z dzielenia
points = 0
for i in range(no_of_reps):
    print(f'porównanie {i+1}')
    print(f'porównuję {word[i]} z {word[-1-i]}')
    if word[i] == word[-1-i]:
        print('OK - znaki są takie same')
        points += 1
    else:
        print('NOK - znaki nie są takie same')

    if points == no_of_reps:
        print('To jest anagram')
    else:
        print('To NIE jest anagram')




