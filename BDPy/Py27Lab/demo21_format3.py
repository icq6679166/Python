# encoding=UTF8
print '[%-20s]' % ('0123456789' * 2)
print '[%-20s]' % ('0123456789'[:5])
print '[%-20s]' % ('中文')
print '[%-20s]' % (u'中文')
print '[{:20s}]'.format('0123456789' * 2)
print '[{:20s}]'.format('0123456789'[:5])
print '[{:20s}]'.format('中文')
print u'[{:20s}]'.format(u'中文')
# extract padding size to variable
print '[%-20s]' % ('0123456789' * 2)
print '[%*s]' % ((-20), '0123456789'[:5])
print '[{:20s}]'.format('0123456789' * 2)
print '[{:{}s}]'.format('0123456789'[:5],20)
