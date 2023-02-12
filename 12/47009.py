for i in range(100):
    for j in range(100):
        for k in range(100):
            stringbegin = '0' + '1'*i + '2'*j + '3'*k + '0'
            string = stringbegin
            while '00' not in string:
                string = string.replace('01', '210', 1)
                string = string.replace('02', '3101', 1)
                string = string.replace('03', '2012', 1)

            if string.count('1') == 61 and string.count('2') == 50 and string.count('3') == 18:
                print(len(stringbegin))
                break