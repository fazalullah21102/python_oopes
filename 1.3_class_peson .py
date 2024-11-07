
class Person:
    def __init__(self ,name , age , selrey, fname ):
        # Initialize attributes with default values
        self.name = name 
        self.age = age
        self.selrey  = selrey 
        self.fname = fname 

    def show_data(self):
        # Print the attributes
        print("My name is:", self.name)
        print("My age is:", self.age)
        print("My fname is:", self.fname)

# Create an instance of the Person class and call the methods
person = Person( "fazalullah" , 18, 120000000, "khan gulab")
person.show_data()
