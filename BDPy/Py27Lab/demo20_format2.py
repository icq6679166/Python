#encoding=UTF8
print '%20s' % ('0123456789' * 2)
print '%20s' % ('0123456789')
print '%20s' % ('中文')
print '%20s' % (u'中文')
print '{:20s}****'.format('0123456789')
print '{:>20s}'.format('0123456789')
print '{:>20s}'.format('中文')
print u'{:>20s}'.format(u'中文')
