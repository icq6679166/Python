class Member:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    def __str__(self):
        return '[%s]%s(%d)' % (self.name, self.location, self.capacity)

    def __repr__(self):
        return '%s' % ({"company name": self.name,
                        "company location": self.location,
                        "company capacity": self.capacity})


class Instructor:
    pass


m1 = Member("ucom", "Taipei", 400)

print "%s, %r" % (m1, m1)
print "{0!s}, {0!r}".format(m1)
