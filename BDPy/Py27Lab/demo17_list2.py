a1 = list('ABCDE')
a2 = list('abcde')
a1.append(a2)
print a1
a3 = list('ABCDE')
a4 = list('abcde')
a3.extend(a4)
print a3
a5 = list('ABCDE')
a6 = list('abcde')
a5 += a6
print a5
a5.reverse()
print a5

