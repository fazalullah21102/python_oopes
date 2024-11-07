"""Create a class named Student that has attributes for name, roll_number, and marks. Write methods to:
Display the student’s details.
Calculate if the student has passed (marks >= 50) or failed."""



class student :
    def __init__(self , name="" , rollno=0, markes=0 ):
        self . name = name 
        self .rollno = rollno
        self.markes = markes
    def detail_display (self):
        print ("My name is : ", self.name)
        print ("RollNo :", self.rollno)
        print("markes:", self.markes)
    def is_passed(self):
        if self.markes > 50 :
            return "pass"
        else:
            return "Fail "
            
s1 = student ("fazalullah" , 161, 89)
s2 = student("abd ullah" , 23, 49)
s1.detail_display()
print ("statue :" , s1.is_passed())
print (" ")
s2.detail_display()
print ("statue :" , s2.is_passed())
 