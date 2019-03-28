def someFunction():
    x=5
    #y=6
    z=7
    y = yield x
    yield y+z

f1 = someFunction()
print f1.next()
print f1.send(100)