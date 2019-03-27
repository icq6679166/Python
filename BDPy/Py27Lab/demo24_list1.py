import copy

a1 = list('ABCDE')
print type(a1), a1
a2 = a1
a3 = list(a1)
a4 = a1[:]
a5 = copy.copy(a1)
a6 = copy.deepcopy(a1)
print a1, a2, a3, a4, a5, a6
print hex(id(a1)), hex(id(a2)), hex(id(a3)), hex(id(a4)), hex(id(a5))
a1[0] = 'a'
a2[1] = 'b'
print a1, a2, a3, a4, a5, a6
