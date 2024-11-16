import math
class triangle :
    def __init__(self , a ,b , c):
        self.num1 = a 
        self .num2 =b
        self.num3 = c
        
    def perimeter (self):
        return  self.num1 + self.num2 + self.num3
        
    def area (self):
        s = self.perimeter()/2
        
        # the used a hereon formula 
        area = math.sqrt ( s *(s - self.num1 ) * (s - self.num2)* (s - self.num3))
        return area 
        
    def find_perimeter_area(self):
        print ("perimeter of ringle is :" , self.perimeter())
        print("area of ringle is : " , self.area())
    
obj = triangle(3,4,5)
obj.find_perimeter_area()




