def sample_func(a, b, c, d, e):
    print 'first element=%s' % (a)
    print 'second element=%s' % (b)
    print 'third element=%s' % (c)
    print 'fourth element=%s' % (d)
    print 'fifth element=%s' % (e)


sample_func('iphone', 'ipad', 'apple watch', 'apple tv', 'beats')
acc = ['apple watch', 'apple tv', 'beats']
sample_func('iphone', 'ipad', *acc)
acc2 = ('iphone', 'ipad', 'apple watch', 'apple tv', 'beats')
sample_func(*acc2)
