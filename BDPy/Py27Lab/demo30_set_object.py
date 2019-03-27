class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __repr__(self):
        return "[%s](%s)" % (self.name, self.duration)

    def __str__(self):
        return repr(self)

    # def __hash__(self):
    #     return hash(self.name + self.duration)

    def __eq__(self, other):
        return self.name == other.name
        AND
        self.duration == other.duration

    pass


c1 = Course("BDPY", "35hr")
c2 = c1
c3 = Course("BDPY", "35hr")
c4 = Course("PYKT", "35hr")
c5 = Course("BDPY", "42hr")
print c1, c2, c3
set1 = {c1, c2, c3, c4, c5}
print set1
