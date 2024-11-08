class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        area = self.length * self.width
        print("The area of the rectangle is:", area)

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)  
        print("The perimeter of the rectangle is:", perimeter)


obj = Rectangle(23, 78)

obj.calculate_area()
obj.calculate_perimeter()
