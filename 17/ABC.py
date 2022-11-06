k = 0
max = 0
with open('ABC.txt') as f:
    file = f.readline()
    for i in range(len(file)):
        if file[i] == "C":
            k += 1
        else:
            if k > max:
                max = k
            k = 0
print(max)
