class Computer:
    def __init__(self, brand, model, processor):
        self.brand = brand
        self.model = model
        self.processor = processor
    
    def specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Processor: {self.processor}")
    def price(self):
        return 500   

class Laptop(Computer):
    def __init__(self, brand, model, processor, battery_life):
        super().__init__(brand, model, processor)
        self.battery_life = battery_life  
    
    def specs(self):
        super().specs()  
        print(f"Battery Life: {self.battery_life} hours")
 
    def price(self):
        base_price = super().price()
        if self.battery_life > 10:
            return base_price + 200 
        else:
            return base_price + 100  

class Desktop(Computer):
    def __init__(self, brand, model, processor, monitor_size):
        super().__init__(brand, model, processor)
        self.monitor_size = monitor_size 
    
    def specs(self):
        super().specs() 
        print(f"Monitor Size: {self.monitor_size} inches")
        
    def price(self):
        base_price = super().price()
        if self.monitor_size >= 27:
            return base_price + 300  
        else:
            return base_price + 150  


laptop = Laptop("Dell", "XPS 13", "Intel i7", 12)
desktop = Desktop("HP", "Pavilion", "AMD Ryzen 5", 24)

print("Laptop Specs:")
laptop.specs() 
print(f"Laptop Price: ${laptop.price()}")  

print("\nDesktop Specs:")
desktop.specs()  
print(f"Desktop Price: ${desktop.price()}") 
