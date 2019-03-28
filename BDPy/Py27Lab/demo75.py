class Emp:
    gradeLevel = 6
    def startWork(self):
        pass
    def endWork(self):
        pass

class RD(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel
    def startWork(self):
        print self.currentGrade, "start R&D"
    def endWork(self):
        print self.currentGrade, "stop R&D"

rd1 = RD()
rd1.currentGrade = 7
rd1.startWork()
print "RD1 grade=", rd1.currentGrade, "RD1 gradelevgel=", rd1.gradeLevel
print Emp.gradeLevel