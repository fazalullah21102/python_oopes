class shape :
    def __init__(self, width , height):
        self.width = width
        self .height = height 
    def area(self):
        pass 
class Triangle (shape):
    def area(self):
        return 2 * self . width  * self .height
class Rectangel(shape):
    def area(self):
        return self.width *self.height 
triangle = Triangle( 10, 5)
rectangel = Rectangel ( 10, 5) 
print ("the area of trinangle  is  :" , triangle. area())
print ("the area of rectange is : " ,rectangel.area())