import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return math.sqrt(x + 3) - x + 1


xArr = np.linspace(0, 6, 20)

for x in xArr:
    print("f({:.3f}) = {:.3f}".format(x, f(x)))

yArr = [f(x) for x in xArr]

print(yArr)

fig = plt.figure()

# rows: 2, columns: 2, graphSerialNumber: 1
ax1 = fig.add_subplot(221)

ax1.plot([1, 2, 3, 4], [10, 20, 25, 30], label='line', color='lightblue', linewidth=3)

ax1.scatter(xArr, yArr, label='f(x)', color='indianred', marker='*')

ax1.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], label='randomPoints', color='darkgreen', marker='^')

ax1.set_xlim(-0.5, 6.5)

ax1.legend()

# rows: 2, columns: 2, graphSerialNumber: 2
ax2 = fig.add_subplot(222)

sinYArr = [math.sin(x) for x in xArr]

ax2.plot(xArr, sinYArr, label='sin(x)', linewidth=4)

ax2.legend()

ax3 = fig.add_subplot(223)

ax3.bar([1, 2, 3], [3, 4, 5], label='barV')

ax3.axhline(2.4)

ax3.legend()

ax4 = fig.add_subplot(224)

ax4.barh([0.5, 1, 2.5], [0, 1, 2], label='barH')

ax4.axvline(1.25)

ax4.legend()

plt.show()

