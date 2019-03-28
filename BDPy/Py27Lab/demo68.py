class Car:
    vendor = "Lexus"
    valid = True


c1 = Car()
print Car.vendor, Car.valid, c1.vendor, c1.valid
Car.function = True
print Car.function, c1.function
c1.color = 'RED'
print c1.vendor, c1.valid, c1.color
c2 = Car()
c2.capacity = 5
print c2.vendor, c2.valid, c2.function, c2.capacity
Car.max = 10000
print c1.max, c2.max, Car.max
