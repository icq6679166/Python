a = 5
b = 7
print 'before, a=', a, ' ,b=', b
temp = a
a = b
b = temp
print 'after, a=', a, ' ,b=', b
c = 6
d = 8
print 'before, c,d=', c, d
c, d = d, c
print 'after c,d=', c, d
e = 'hello world'
f = 3.14
print 'before, e,f=', e, f
e, f = f, e
print 'after, e,f=', e, f
g, h, i, j, k = 'A', 'K', 'Q', 'J', '10'
g, h, i, j, k = g, i, k, h, j
print 'result=', g, h, i, j, k
