class Factorial:
    def factorial_find(self):
        num1 = int(input("Enter a number: "))
        fact = 1
        for i in range(num1, 1, -1):
            fact *= i 
        print("Factorial of the given number is:", fact)
obj = Factorial()
obj.factorial_find()
