class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_quantity(self):
        return self.quantity
    
    def update_quantity(self, quantity):
        if self.quantity - 1 < 0:
            print("Barang Sudah Tidak Tersedia")
            return False
        else:
            self.quantity -= 1
            return True
        
class Electronics(Product):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    def get_warranty_period(self):
        return self.warranty_period

class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def get_size(self):
        return self.size

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def get_author(self):
        return self.author
    

class Cart:
    def __init__(self):
        self.item = []

    def add_to_cart(self, product):
        for i in self.item:
            if i['name'] == product['name']:
                i['quantity'] += 1
                return True
        self.item.append(product)

    def remove_from_cart(self, product):
        self.item.pop(product - 1)
        return True
    
    def view_cart(self):
        x = 1
        for i in self.item:
            print(x,".", i['name'], "Harga : ", i['price'], "Quantity: ", i['quantity'])
            x += 1
    def place_order(self):
        jumlah = 0

        for i in self.item:
            jumlah += (i['price'] * i['quantity'])
        print('Ringkasan Order: ', jumlah)
        print("Terimakasih Telah Berbelanja :)")


cart = Cart()

product1 = Electronics('Iphone X (ELectronics)', 5000000, 5, 1)
product2 = Electronics('Poco M4 Pro (ELectronics)', 2800000, 10, 2)
product3 = Clothing('Adidas Ultraboost Shoes (Clothing)', 500000, 10, 8)
product4 = Book('HAIKYU FYL HIGH VOLLEYBALL (Book)', 35000, 10, 'Haruichi Furudate')