class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
print("Addition:", MathOperations.add(3, 5))      
print("Subtraction:", MathOperations.subtract(10, 4))  
print("Multiplication:", MathOperations.multiply(6, 7)) 
print("Division:", MathOperations.divide(8, 2))      
print("Division by Zero:", MathOperations.divide(8, 0)) 
