str1 = 'abcdefg1234567890'
print str1[len(str1) - 1]
# print str1[len(str1)]
print str1[-len(str1)], str1[0]
print str1[2:10]
str2 = "www.uuu.com.tw"
return1 = str2.split(".")
print type(return1)
print return1
print "@".join(return1)
print "".join(return1)
print str1+str2
print str2*5
print 5*str2
print 'abc' in str1, 'ABC' not in str1