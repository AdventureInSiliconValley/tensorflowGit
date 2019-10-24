import numpy as np

# 说明：新加一个苹果的时候（比如从三个增加到四个），你可以用，也可以不用。如果你使用这个苹果，那么就等于四个苹果全部用（因为如果只是使用三个或者更少苹果的话，那么等于没有用到第四个苹果），那么总数已经有四个苹果了，其他的份数可以由梨和桃子补充。如果你没有使用这个苹果，那么总数还是由三个苹果、梨和桃子补充。四个苹果和其他固定数量的梨和桃子由这两个数之和获得。
# 但是你可以这样子想象，如果你有三个菜品，那么两个菜品数量一样的情况下，第三个菜品增加，如何从已有菜品导出？如果是两个菜品呢？如果第三个菜品数目为0，不就是两个菜品？如果两个菜品都知道，第三个菜品可以一次加一，加到任意数目。

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
