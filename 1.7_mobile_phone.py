class MobilePhone:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_life = battery_life

    def show_detail(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price: $", self.price)
        print("Battery Life:", self.battery_life, "hours")

obj = MobilePhone("Samsung", "Galaxy S21", 799.99, 20)
obj.show_detail()
budget = 100
if budget > obj.price:
    print("The phone is affordable within a budget of $", budget)
else:
    print("The phone is not affordable within a budget of $", budget)
