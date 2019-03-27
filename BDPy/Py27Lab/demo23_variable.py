foo = 38
age = 38
print "when age=38, age id=%s, and foo id=%s" % (hex(id(age)), hex(id(foo)))
bar = 39
age = 39
print "when age=39, age id=%s, and bar id=%s" % (hex(id(age)), hex(id(bar)))


class Person:
    def __init__(self, age):
        self.age = age


p1 = Person(38)
print "when p1 initialized, p1 id=%s, p1.age id=%s" % (hex(id(p1)), hex(id(p1.age)))
p1.age = 39
print "when p1 assign to 39, p1 id=%s, p1.age id=%s" % (hex(id(p1)), hex(id(p1.age)))
