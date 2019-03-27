# encoding=UTF-8
print '{:<10}==='.format('ABC')
print '{:0<10}==='.format('ABC')
print '{:_<10}==='.format('ABC')
print '{:\'<10}==='.format('ABC')
print '{:\\<10}==='.format('ABC')

print '%.6s' % ('這是一個非常長的字串')
print '%.*s' % (6, '這是一個非常長的字串')
print '%.8s' % ('這是一個非常長的字串')
print '%.6s' % (u'這是一個非常長的字串')
print '{:.6s}'.format('這是一個非常長的字串')
print u'{:.6s}'.format(u'這是一個非常長的字串')
print u'{:.{}s}'.format(u'這是一個非常長的字串', 6)
