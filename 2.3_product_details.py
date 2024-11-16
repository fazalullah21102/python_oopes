class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price}")

class Electronics(Product):
    def __init__(self, product_name, price, warranty):
        super().__init__(product_name, price)
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Warranty: {self.warranty} years")
        
product = Electronics("Laptop", 1200, 2)
product.display()
