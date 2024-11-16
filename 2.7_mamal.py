class Mammals:
    def display_mammal(self):
        print("I am a mammal")

class MarineAnimals:
    def display_marine_animal(self):
        print("I am a marine animal")
class BlueWhale(Mammals, MarineAnimals):
    def display_blue_whale(self):
        print("I belong to both the categories: Mammals as well as Marine Animals")
mammal = Mammals()
marine_animal = MarineAnimals()
blue_whale = BlueWhale()    
mammal.display_mammal()
marine_animal.display_marine_animal()
blue_whale.display_blue_whale()
blue_whale.display_mammal()        
blue_whale.display_marine_animal() 

