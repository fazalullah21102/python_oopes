class employ:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"position: {self.position}")

class manager(employ):
    def __init__(self, name, age, position, department):
        super().__init__(name, age, position)
        self.department = department  

    def display(self):
        super().display()
        print("department:", self.department) 
        
s1 = employ("Fazalullah", 18, "Software Developer")
s1.display()
print (" ")
s2 = manager("Abdullah", 19, "Project Manager", "AI")
s2.display()
