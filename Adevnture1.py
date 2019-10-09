import numpy as np

a = np.arange(15).reshape(3, 5)

# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]] 2 int32 4 15 <class 'numpy.ndarray'>
print(a, a.ndim, a.dtype.name, a.itemsize, a.size, type(a))

b = np.array([6, 7, 8])

print(b, type(b))

c = np.array([2.1, 1.3, 5.5])

print(c, type(c), c.dtype)

d = np.array([[1, 2], [3, 4]], dtype=complex)

print(d)

e = np.array([(1, 3), (4, 9)])

print(e)

f = np.zeros((3, 4))

print(f)

g = np.ones((2, 3, 4), dtype=np.int16)

print(g)

h = np.empty((2, 3))

print(h)

i = np.arange(10, 30, 5)

print(i)

k = np.arange(0, 2, .3)

print(k)

j = np.linspace(0, 2, 9)
print(j)

l1 = np.linspace(0, 2 * np.pi, 100)

print(l1)

m = np.sin(l1)

print(m)

n = np.arange(24)

print(n)

r = n.reshape(2, 3, 4)

print(r)


