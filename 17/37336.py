count = 0
max_sum = -20001
with open('17.txt') as f:
    numbers = list(map(int, f.readlines()))
    for i in range(len(numbers) - 1):
        if numbers[i] % 3 == 0 or numbers[i + 1] % 3 == 0:
            count += 1
            max_sum = max(max_sum, numbers[i] + numbers[i + 1])
print(count, max_sum)