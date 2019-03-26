str1 = 'abcdeABCDE12345'
str2 = str1 * 5
print str2[1:20:2]
print len(str1), len(str2), len(str2[1:30:3])
print min(str2), max(str2)
print str2.index('a'), str2.index('A'), str2.index('1')
#print str2.index('X')
print str2.count('X'), str2.count('a')
