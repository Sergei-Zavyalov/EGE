max = 0
count = 0
max_num = 0
with open('47221.txt') as f:
    numbers = list(map(int, f.readlines()))
    for i in range(len(numbers)):
        if numbers[i] > max_num and abs(numbers[i]) % 10 == 3:
            max_num = numbers[i]
    max_num = max_num ** 2
    for i in range(len(numbers) - 1):
        if abs(numbers[i]) % 10 == 3 and abs(numbers[i+1]) % 10 != 3 or \
                abs(numbers[i]) % 10 != 3 and abs(numbers[i+1]) % 10 == 3:
            if (numbers[i] ** 2) + (numbers[i + 1] ** 2) >= max_num:
                count += 1
                if (numbers[i] ** 2) + (numbers[i + 1] ** 2) > max:
                    max = numbers[i] ** 2 + numbers[i + 1] ** 2
print(count, max)
