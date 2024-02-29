ls25 = [i for i in range(1,26)]
def matricize(x):
    sqrt = int(len(x) ** 0.5)
    matrix = []
    while x != []:
        matrix.append(x[:sqrt])
        x = x[sqrt:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = '?'

    return matrix

print(matricize(ls25))