class Member:
    def __init__(self):
        self.name = 'ucom'
        self.location = 'taipei'
        self.capactity = 400
        pass

    def __str__(self):
        return '[%s]%s(%d)' % (self.name, self.location, self.capactity)

    @property
    def __repr__(self):
        return '%s' % ({"company name": self.name,
                        "company location": self.location,
                        "company capactity": self.capactity})


m1 = Member("ucom", "Taipei",400)
print "%s,"
