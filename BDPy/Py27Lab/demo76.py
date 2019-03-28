class Emp:
    pass


class Engineer(Emp):
    pass


class PM(Emp):
    pass


class HR(Emp):
    pass


emp1 = Emp()
eng1 = Engineer()
pm1 = PM()
hr1 = HR()
staffs = [("emp1", "emplyee1"), (eng1, "engineer1"),
          (pm1, "Product Manager"), (hr1, "Human Resource1")]
classes = [Emp, Engineer, PM, HR]

for staff, name in staffs:
    for emp_class in classes:
        isA = isinstance(staff, emp_class)
        msg1 = 'is a' if isA else 'is not a'
        print name, msg1, emp_class.__name__

for class1 in classes:
    for class2 in classes:
        isSubclass = issubclass(class1, class2)
        message = '{0} a subclass of'.format('is' if isSubclass else 'is not')
        print class1.__name__, message, class2.__name__
