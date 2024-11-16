class Rectangle:
    name = "fazalullah"
    age = 18
    gpa = 3.44

    @classmethod
    def change(cls):
        # Print class variables
        print("Name:", cls.name)
        print("Age:", cls.age)
        print("GPA:", cls.gpa)
        print("Class method value:")

# Call the class method
Rectangle.change()
