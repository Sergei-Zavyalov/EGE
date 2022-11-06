import itertools

listString = itertools.product('ВИШНЯ', repeat=6)

count = 0
for str in listString:
    line = ''.join(str)
    if line.count('В') <= 1 and line[0] != 'Ш' and line[-1] != 'И' and line[-1] != 'Я':
        count += 1
        print(line)

print(count)