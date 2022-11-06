import itertools

listString = itertools.product('ШКОЛА', repeat=3)

count = 0
for str in listString:
    line = ''.join(str)
    if line.count('К') == 1:
        count += 1
print(count)
