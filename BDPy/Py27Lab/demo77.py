def someFunction():
    a = 1
    b = 2
    yield a
    a += b
    yield a

print someFunction()
f1 = someFunction()
print 'first time', f1.next()
print 'second time', f1.next()
#print f1.next()
print someFunction().next()
print someFunction().next()
print someFunction().next()