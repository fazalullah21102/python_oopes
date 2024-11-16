class shape :
    def display (self):
        print ("this is a shape ")
class polygon (shape):
    def display (self):
        print ("polygon is a shape ")
class Rectangel:
    def display (self):
        print ("rctangel is polygon ")
class triangle :
    def display (self):
        print ("this  is a triangle  is polygon")
class squre :
    def display (self):
        print ("squre is ractangle")


s1 = shape()
s1.display()

s2 = polygon()
s2.display()

s3 = Rectangel()
s3.display()

s4=triangle()
s4.display()

s5 = squre()
s5.display()
    
    