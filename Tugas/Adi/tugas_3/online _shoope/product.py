# class product

class product:
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getQuantity(self):
        return self.quantity
    
    def updateQuantity(self, quantity):
        self.quantity += quantity
        

class Electronics(product):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, price, quantity)
        self.warranty_period = int(warranty_period)

    def get_warranty_period(self):
        return self.warranty_period
    

class Cloathing(product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = str(size)

    def getSize(self):
        return self.size
    

class Book(product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = str(author)
 
    def getAuthor(self):
        return self.author
    
#object
Solo_Leveling = Book("Solo Leveling", 150000, 9, "Chugong")
Iphone_XR = Electronics("Iphone XR", 1400000, 12, 12)
Sarung_GajahDuduk = Cloathing("Sarung gajah duduk", 89000, 20, "L")