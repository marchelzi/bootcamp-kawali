class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
            return self.name

    def get_price(self):
            return self.price

    def get_quantity(self):
            return self.quantity

    def update_quantity(self,quantity):
        if self.quantity - 1 < 0:
            print('Barang sudah tidak tersedia')
            return False
        else:
             self.quantity -= 1
             return True
      
class Electronic(Product):
    def __init__(self,name,price,quantity,warraty_period):
        super().__init__(name,price,quantity)
        self.warraty_period = warraty_period

    def get_warraty_period(self):
        return self.warraty_period
 
class Clothing(Product):
    def __init__(self, name, price, quantity,size):
        super().__init__(name, price, quantity)
        self.size = size

    def get_size(self):
        return self.size 


class Book(Product):
    def __init__(self, name, price, quantity,author):
        super().__init__(name, price, quantity)
        self.author = author

    def get_author(self):
        return self.author

class Cart:
    def __init__(self):
        self.items = []

        # def get_items(self):
        #     self.items = items

    def add_to_cart(self,product):
        for i in self.items:
            if i['name'] == product['name']:
                i['quantity'] += 1
                return True
        self.items.append(product)

    def remove_from_cart(self,product):
            self.items.pop(product - 1)

    def view_cart(self):
        x = 1
        for i in self.items:
            print(x, i['name'],'Harga:', i['price'],'Kuantiti: ', i['quantity'])
            x += 1

    def place_order(self):
            jumlah = 0

            for i in self.items:
                 jumlah += (i['price'] * i['quantity'])
            print('Ringkasan Order: ', jumlah)
            print('Terimakasih Telah Berbelanja')


cart = Cart()

product_1 = Electronic('Samsung (Electronic)', 7000000,5,1)
product_2 = Electronic('Xiaomi (Electronic)', 6000000,5,2)
product_3 = Clothing('Adidas Ultraboost Shoes (Clothing)', 400000,15,8)
product_4 = Book('The Catcher In The Rye(Book)', 400000,15,'J.D Salinger')



