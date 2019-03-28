class Group(object):
    def __init__(self):
        print("initial function")
        self.counter = 0
    def __iter__(self):
        print("start to iterate")
        return self
    def __next__(self):
        if self.counter < 10:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration()
    pass


g1 = Group()
for i in g1:
    print("***",i)
print(type(g1))