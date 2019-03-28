class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.member * self.day

    @staticmethod
    def calculate(x, y):
        return x ** y

    @classmethod
    def get_member(cls):
        return cls.member


t1 = Team()
print "all working hour=", t1.all_working_hour()
print "working hour=", t1.working_hour()
print Team.calculate(2, 3)
print t1.calculate(3, 2)
print Team.get_member(), t1.get_member()
