matrix = [[2, -6, -1, -38],
          [-3, -1, 7, -34],
          [-8, 1, -2, -20]]


def rowOp(down, up, k):
    global matrix
    for e in range(len(matrix[0])):
        matrix[down][e] -= k * matrix[up][e]


def gauss():
    global matrix
    for i in range(len(matrix)):
        rowOp(i, i, 1-1/matrix[i][i])
        for j in range(i, len(matrix)):
            if j != i:
                rowOp(j, i, matrix[j][i])


gauss()
print(matrix)

# Raw result: [[1.0, -3.0, -0.5, -19.0], [0.0, 1.0, -0.5500000000000007, 9.100000000000009], [0.0, 0.0, 1.0, -2.000000000000014]]

# z = -2
# y = 8
# x = 4
'''
Estabilidade externa
    [0.442]
    [0.615]
    [-0.109]

Estabilidade interna
    [0.0]
    [0.0]
    [0.0]
'''