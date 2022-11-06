k = 0
max = 0
with open('LDR.txt') as f:
    file = f.readline()
    for i in range(len(file)-2):
        if file[i] == "L" and file[i+1] == "D" and file[i+2] == "R":
            k += 3

        else:
            if file[i] == "L":
                k += 1
                if file[i+1] == "D":
                    k += 1
            if k > max:
                max = k
                k = 0
print(max)