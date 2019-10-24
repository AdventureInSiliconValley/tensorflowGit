# encoding:utf-8
import numpy as np

# 说明：新加一个苹果的时候（比如从三个增加到四个），你可以用，也可以不用。如果你使用这个苹果，那么就等于四个苹果全部用（因为如果只是使用三个或者更少苹果的话，那么等于没有用到第四个苹果），那么总数已经有四个苹果了，其他的份数可以由梨和桃子补充。如果你没有使用这个苹果，那么总数还是由三个苹果、梨和桃子补充。四个苹果和其他固定数量的梨和桃子由这两个数之和获得。
# 但是你可以这样子想象，如果你有三个菜品，那么两个菜品数量一样的情况下，第三个菜品增加，如何从已有菜品导出？如果是两个菜品呢？如果第三个菜品数目为0，不就是两个菜品？如果两个菜品都知道，第三个菜品可以一次加一，加到任意数目。
# 简单来说，就是先让苹果数目为0，算出所有梨和桃子的组合。最后依次增加苹果的数目。
# 如果不是三道菜，而是四道菜。那么就是让第四道菜为0，用刚刚的办法算出三道菜的所有组合。依次增加第四道菜。
# 同理，五道菜，六道菜也一样。
# 因为我的编程能力没有我想象中那么好。但是我提供一个思路：对于每个算出来的梨和桃子组合（苹果为0的时候），把苹果从1算到5。
# 就算再加无数道菜，都是先把想到算的那道设置为0，算出前面几道菜的组合。然后把前面几道菜的组合遍历，把想要算的菜从1算到任意数字。
# 仅仅提供一个不成熟的思路，怕大家昨天没有看懂。如果有不便之处，请包涵。
# 免责声明：仅仅提供参考。不能保证公式和提供的部分代码无误，不提供任何担保。一切商业用途和产生的后果和作者本人无关。不提供法律追溯的权力。

m = np.zeros((9, 6, 5, 4))

# For a total combination number of 0, all combinations of the three dishes can have one way to do it.
# It's the first boundary condition.
m[0][:] = 1

# Second dish and third dish with value of 0.
# For all the numbers of the first dish, find the number of total combinations.
for i in range(1, 9):
    for j in range(1, 6):
        if j >= i:
            m[i][j][0][0] = 1

# Third dish of number 0.
# For every number of the first dish, find the total number of combinations for the second dish with number from 1 to 4.
# The so-called 'either not use it or use it all' strategy.
# Now we have the number of total combinations for every combination of the first and the second dish
#  when the third dish is with number 0.
for i in range(1, 9):
    for j in range(1, min(i + 1, 6)):
        for k in range(1, min(i + 1, 5)):
            m[i][j][k][0] += m[i][j][k - 1][0] + m[i - k][j][0][0]

# For every combination of the first and second dish,
# find the total number of combinations for the third dish with number from 1 to 3.
for i in range(1, 9):
    for j in range(1, min(i + 1, 6)):
        for k in range(1, min(i + 1, 5)):
            for n in range(1, min(i + 1, 4)):
                m[i][j][k][n] += m[i][j][k][n - 1] + m[i - n][j][k][0]


# m[2][1][1][2] = m[2][0][1][2] + m[1][0][1][2]
print(m[2][1][:])
print(m[8][5][4][3])
