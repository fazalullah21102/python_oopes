class largest_no :
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2= num2
        self.num3 = num3
    def check (self):
        if self.num1 > self.num2 and self.num1 > self.num3:
            print ("num1  is greater number : ", self.num1)
        elif self.num2 > self.num3:
            print ("num2 is greater number : ", self.num2)
        else:
            print ("num3 is greater number : " , self.num3)
obj = largest_no (34, 65, 34)
obj.check()
    
