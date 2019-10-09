import numpy as np

a = [1, 2, 3]
b = [4, 5, 6]

c = zip(a, b)

for e1, e2 in c:
    print(e1, e2)

print(np.dot(a, b))

d = np.array([1, 2, 3])
e = np.array([4, 5, 6])

print(np.dot(d, e))
