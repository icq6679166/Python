day_of_week = ('Sunday', 'Monday')
print hex(id(day_of_week))
day_of_week += ('Tuesday',)
print hex(id(day_of_week))
print day_of_week

print (('Wednesday') * 5)
print (('Wednesday',) * 5)
print day_of_week[0], day_of_week[2]


# print day_of_week[4]
def split_head(seq):
    print "seq id=", hex(id(seq))
    return seq[0], seq[1:]


list1 = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print "list1 id=", hex(id(list1))
first, remaining = split_head(list1)
print type(first), first
print type(remaining), remaining
