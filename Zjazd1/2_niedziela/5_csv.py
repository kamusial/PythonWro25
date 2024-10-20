#1. Odczyt csv z zapisem poszczególnych pól

# with open('rozliczenie.csv', 'r') as file1:
path = 'rozliczenie.csv'
mode = 'r'
with open(path, mode) as file_csv:
    content = file_csv.readlines()
print(content)
print(content[4])
for i in range(len(content)):



