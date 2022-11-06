max_sum = 0
count = 0
with open('17-a.txt') as f:
    numbers = list(map(int, f.readlines()))
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if ((numbers[i] + numbers[j]) % 2 == 1) and (numbers[i] * numbers[j]) % 5 == 0:
                count += 1
                max_sum = max(max_sum, numbers[i] + numbers[j])

print(count, max_sum)

