class animal :
    def __init__(self, name , age ):
        self.name = name
        self.age = age 
    
class zabra (animal):
    def display (self):
        print ("zebra _ name : " , self.name , "age : " , self.age,  " Origin: Africa")
class dolpan  (animal):
    def display (self):
        print(f"dolpan _name {self.name} age {self.age} Origin: Oceans worldwide")
        
s1 = zabra("Zara", 5)
s1.display()
s2 = dolpan("Flipper", 8)
s2.display()