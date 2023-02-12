k = 0
maxk = 0
maxi = 0
particles = open("26-47023.txt").readlines()[1:]
matrix = [[0 for i in range(10001)] for j in range(10001)]
for i in range(len(particles)):
    particles[i] = list(map(int, particles[i].split(' ')))
    matrix[particles[i][0]][particles[i][1]] = 1
for i in range(10001):
    j = 0
    while j < 9999:
        if str(matrix[i][j]) + str(matrix[i][j + 1]) == '10':
            k += 1
            j += 2
        else:
            prevmaxk = maxk
            maxk = max(maxk, k)
            if prevmaxk != maxk:
                maxi = i
            k = 0
            j += 1
print(maxk, maxi)
