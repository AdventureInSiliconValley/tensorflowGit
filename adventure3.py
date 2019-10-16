import numpy as np

print(np.linspace(0, 2, 9))

print(np.linspace(0, 2 * np.pi, 100))

print(np.arange(10000).reshape(100, 100))

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print(A.dot(B))

print(np.dot(A, B))

a = np.ones((2, 3), dtype=int)

print(a)

b = np.random.random((2, 3))

print(b)

a *= 3
print(a)

b += a
print(b)

c = a + b

print(c)

print(c.dtype.name)

# Same as d = np.power(np.e, c * 1j)
d = np.exp(c * 1j)

print(d)

e = np.power(np.e, c * 1j)

print(e)

print(e.dtype.name)

f = np.random.random((2, 3))

f.sum()
f.max()
f.min()

print(f.cumsum(axis=1))


