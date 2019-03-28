class Group(object):
    def __init__(self):
        print "initial function"
        self.counter = 0
    def __iter__(self):
        print "start to iterate"
        return self
    def next(self):
        print "iterate to next"
        raise StopIteration()
    pass


g1 = Group()
for i in g1:
    print g1
print type(g1)