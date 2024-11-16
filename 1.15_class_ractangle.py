class Area:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def return_area(self):
        return self.length * self.breadth

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

rectangle = Area(length, breadth)

print("The area of the rectangle is:", rectangle.return_area())
