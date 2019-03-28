class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rect1 = Rectangle(3, 2)
print rect1.calculate_area()
rect2 = Rectangle(4, 6)
print rect2.calculate_area()
