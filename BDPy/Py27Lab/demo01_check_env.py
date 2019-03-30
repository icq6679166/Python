import numpy as np

print np.__version__

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

print type(l1), type(l2)
print l1 + l2, l2 + l1
a1 = np.array(l1)
a2 = np.array(l2)
print type(a1), type(a2)
print a1 + a2, a2 + a1
