length = 0
max_len = 0
with open("47228.txt") as f:
    string = str(f.readlines())
    for i in range(len(string)-1):
        if ((string[i] == 'D' or string[i] == 'F' or string[i] == 'C') and (string[i + 1] == 'A' or string[i + 1] == 'O')) or \
                ((string[i + 1] == 'D' or string[i + 1] == 'F' or string[i + 1] == 'C') and (string[i] == 'A' or string[i] == 'O')):
            length += 1
        else:
            if length > max_len:
                max_len = length
            length = 0
print(max_len // 2)

