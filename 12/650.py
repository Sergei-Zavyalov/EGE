string = '>' + '1' * 25 + '2' * 17 + '3' * 10

while '>1' in string or '>2' in string or '>3' in string:
    if '>1' in string:
        string = string.replace('>1', '22>3', 1)
    if '>2' in string:
        string = string.replace('>2', '2>', 1)
    if '>3' in string:
        string = string.replace('>3', '11>2', 1)

sumnum = 0
for i in range(len(string)):
    if string[i] != '>':
        sumnum += int(string[i])
print(sumnum)
