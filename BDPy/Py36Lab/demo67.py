class MyClass:
    pass


inst1 = MyClass()

print("inst1 type is:", type(inst1))
print("inst1 class is:", inst1.__class__)
print("inst1 class base:", inst1.__class__.__bases__)
print("is inst1 type equal?", type(inst1) == MyClass)
print("is inst1 class equal?", inst1.__class__ == MyClass)
