import itertools

listString = itertools.product('БОРИС', repeat=6)
count = 0
for str in listString:
    line = ''.join(str)
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)