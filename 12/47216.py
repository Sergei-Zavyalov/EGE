for n in range(100000):
    str = '>'
    sum = 0
    state = True
    for i in range(39):
        str += '0'
    for i in range(n):
        str += '1'
    for i in range(39):
        str += '2'

    while str.find('>1') != -1 or str.find('>2') != -1 or str.find('>0') != -1:
        if str.find('>1') != -1:
            str = str.replace('>1', '22>')
        if str.find('>2') != -1:
            str = str.replace('>2', '2>')
        if str.find('>0') != -1:
            str = str.replace('>0', '1>')
    str = str.replace('>', '')
    for i in range(len(str)):
        sum += int(str[i])
    for i in range(2, sum // 2):
        if sum % i == 0:
            state = False
    if state:
        print(n)
        break

