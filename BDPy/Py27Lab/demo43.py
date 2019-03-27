import itertools

l1 = list('ABC')
l2 = list('XYZ')
l3 = list('PQR')
result1 = itertools.chain(l1, l2, l3)
result_list1 = [i for i in result1]
print len(result_list1), result_list1, result_list1
l4 = ['Spyder Man','Bat Man','Super Man','Iron Man']
result2 = [l for l in itertools.permutations(l4, 3)]
print len(result2), result2
l5 = ['Kingston','micron','samsung','transand','intel']
result3 = [l for l in itertools.combinations(l5, 2)]
print len(result3), result3
