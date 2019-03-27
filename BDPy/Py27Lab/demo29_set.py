set1 = {'A', 'P', 'P', 'L', 'E'}
set2 = set(list('BANANA'))
print set1
print set2
print len(set1)
print set1 | set2
print set1 & set2
print set1 ^ set2
print (set1 ^ set2) | (set1 & set2)
set1.add('X')
#set1.add(set2)
print set1
for element in set2:
    set1.add(element)
print set1
