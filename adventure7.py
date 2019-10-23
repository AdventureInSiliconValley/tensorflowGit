import numpy as np

m = np.zeros((9, 6, 5, 4))

m[0][:] = 1

for i in range(1, 9):
    for j in range(1, 6):
        if j >= i:
            m[i][j][0][0] = 1

for i in range(1, 9):
    for j in range(1, 5):
        if j >= i:
            m[i][0][j][0] = 1

for i in range(1, 9):
    for j in range(1, 4):
        if j >= i:
            m[i][0][0][j] = 1

for i in range(1, 9):
    for j in range(1, min(i + 1, 6)):
        for k in range(1, min(i + 1, 5)):
            m[i][j][k][0] += m[i][j - 1][k][0] + m[i - j][0][k][0]

for i in range(1, 9):
    for k in range(1, min(i + 1, 5)):
        for n in range(1, min(i + 1, 4)):
            print(i, k, n, m[i][0][k - 1][n], m[i - k][0][0][n])
            m[i][0][k][n] += m[i][0][k - 1][n] + m[i - k][0][0][n]

for i in range(1, 9):
    for j in range(1, min(i + 1, 6)):
        for n in range(1, min(i + 1, 4)):
            m[i][j][0][n] += m[i][j - 1][0][n] + m[i - j][0][0][n]

for i in range(1, 9):
    for j in range(1, min(i + 1, 6)):
        for k in range(1, min(i + 1, 5)):
            for n in range(1, min(i + 1, 4)):
                m[i][j][k][n] += m[i][j][k][n - 1] + m[i - n][j][k][0]


# m[2][1][1][2] = m[2][0][1][2] + m[1][0][1][2]
print(m[2][1][:])
print(m[8][5][4][3])
