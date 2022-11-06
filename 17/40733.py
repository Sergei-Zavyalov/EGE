count = 0
avg = 0
max_sum = 0
with open('17 (1).txt') as f:
    numbers = list(map(int, f.readlines()))
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            avg += numbers[i]
            count += 1
    avg = avg / count
    count = 0
    for i in range(len(numbers) - 1):
        if (numbers[i] % 3 == 0 or numbers[i + 1] % 3 == 0) and (numbers[i] < avg or numbers[i + 1] < avg):
            count += 1
            max_sum = max(max_sum, numbers[i] + numbers[i + 1])
print(count, max_sum)

