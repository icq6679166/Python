# encoding=UTF-8
p1 = u'中文輸入'

print repr(p1)
print repr(p1.encode('utf8'))
print repr(p1.encode('utf16'))
print repr(p1.encode('ms950'))
print repr(p1.encode('big5'))

new_s1 = '\xe5\xad\x97'
print new_s1, repr(new_s1)
print new_s1.decode('latin-1')
print new_s1.decode('utf-8')
