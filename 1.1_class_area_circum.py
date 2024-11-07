class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    
    
    def area(self):
        pi = 3.14159
        area_find = pi * (self.radius ** 2) 
        print("Area of circle is:", area_find)
        
    def circum(self):
        pi = 3.14159
        circumference = 2 * pi * self.radius  
        print("Circumference of circle is:", circumference)
        
obj = Circle(34)
obj.area()
obj.circum()
