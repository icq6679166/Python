l1 = list("ABCDEFG1234567")
l2 = list("ABCDEFG1234567" * 2)
l1[0] = '*'
print l1
l1[:5] = '!' * 3
print l1
del l1[:5]
print l1
l2[::2] = '%' * len(l2[::2])
print l2
del l2[1::2]
#del l2[::2]
print l2
