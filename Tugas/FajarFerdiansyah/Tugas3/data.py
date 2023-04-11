class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.prince = price
        self.quantity = quantity

    def get_name(self):
            return self.name

    def get_price(self):
            return self.prince

    def get_quantity(self):
            return self.quantity

    def update_quantity(self, quantity):
        if self.quantity - 1 <0:
             print('Barang sudah tidak tersedia')
             return False
        else:
             self.quantity -= 1
             return True

class Electronics(Product):
    def  __init__(self, name, price, quantity, warranty_period):
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

class Cart():
    def __init__(self):
        self.item = []
        

    def add_to_cart(self, product):
        for i in self.item:
            if i['name'] == product['name']:
                i['quantity'] += 1
                return True
        self.item.append(product)

    def remove_from_cart(self, product):
        pass

    def view_cart(self):
        x = 1
        for i in self.item:
             print(x, i['name'], "Harga", i['price'],"Quantity", i['quantity'])
             x += 1

    def place_order(self):
        jumlah = 0

        for i in self.item:
             jumlah +=(i['price'] * i['quantity'])
        print('Ringkasan Order: ', jumlah)
        print('Terimakasih Telah Berbelanja')


cart = Cart()

product_1 = Electronics('Samsung (Electronics)', 7000000, 5, 1)
product_2 = Electronics('Xiomi (Electronics)', 600000000, 5, 2)
product_3 = Clothing('Adidas Ultraboost Shoes (Clothing)', 400000, 5, 8)
product_4 = Book('The Catcher In The Rye(Clothing)', 400000, 5,'J.D Salinger')
