class Marks:
    def __init__(self):
        self.marks1=0
        self.marks2=0
        self.marks3=0
    def in_data(self):
        self.marks1 = int (input ("enter a first marks :"))
        self.marks2 = int (input ("enter a second marks :"))
        self.marks3 = int (input ("enter a  second marks :"))
    def sum (self):
       return self.marks1 +self.marks2+ self.marks3
    def avg (self):
        return self.sum()/3
    student = Marks()
    student.in_data()
    print("the sum of all marks is : ", student.sum())
    print("the avg marks is :" , student.avg())