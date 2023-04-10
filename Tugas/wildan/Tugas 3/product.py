#class product
#class electronic(child of product class)


class product:

    def __init__(self, name, price, quantity):
        self.name =str(name)
        self.price = float(price)
        self.quantity = int(quantity)

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getQuantity(self):
        return self.quantity
    
    def updateQuantity(self, jml):
        self.quantity += jml


class electronics(product):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, price, quantity)
        self.warranty_period =int( warranty_period)

    def getWarrantyPeriod(self):
        return self.warranty_period
    
class clothing(product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = str(size)

    def getSize(self):
        return self.size
    
    
class book(product):
    def __init__(self, name, price, quantity, auothor):
        super().__init__(name, price, quantity)
        self.auothor = str(auothor)

    def getAuothor(self):
        return self.auothor
    
    # object

Surga_Dan_Neraka = book(' Surga Dan Neraka', 20000, 50, 'Uman Rusmana')
Sepatu_Compass = clothing(' Sepatu Compass', 575000, 10, '39' )
TV_Samsung = electronics(' TV Samsumg', 6000000, 5, 6)


