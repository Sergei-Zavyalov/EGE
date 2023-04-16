import re

matrix = ["0" * 100001 for j in range(100001)]
f = open('СтатГрад.txt')
f.readline()
for line in f:
    x, y = map(int, line.split())
    matrix[x] = matrix[x][:y] + '1' + matrix[x][y + 1:]
max_lines = 0
row_number = 0
for i in range(100001):
    line_count = 0
    count = 0
    items = re.split(r"[0]+", matrix[i])
    while '' in items:
        items.remove('')
    while '1' in items:
        items.remove('1')
    while '11' in items:
        items.remove('11')
    if len(items) >= max_lines:
        max_lines = len(items)
        row_number = i
print(max_lines, row_number)
