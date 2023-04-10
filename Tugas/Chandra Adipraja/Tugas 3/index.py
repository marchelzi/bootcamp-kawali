class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_name(self):
        return self.name
    def get_price(self):
        return float(self.price)
    def get_quantity(self):
        return self.quantity
    def update_quantity(self, quantity):
        if self.quantity - 1 < 0:
            print('Product Is Not Avaible ')
            return False
        else:
            self.quantity -= 1
            return True

class Electronics(Product):
    def __init__(self,name,price,quantity,warranty_period):
        super().__init__(name,price,quantity)
        self.warrperiod = warranty_period

    def get_warranty_period(self):
        return self.warrperiod
class Clothing(Product):
    def __init__(self,name,price,quantity,size):
        super().__init__(name,price,quantity)
        self.size = size
    def get_size(self):
        return self.size

class Book(Product):
    def __init__(self,name,price,quantity,author):
        super().__init__(name,price,quantity)
        self.author = author
    def get_author(self):
        return self.author

class Cart():
    def __init__(self):
        self.items = []
    def add_to_cart(self,item):
        for j in self.items:
            if j['name'] == item['name']:
                j['quantity'] += 1
                print('product add to cart',item['name'])
                return False
        self.items.append(item)
        print('product add to cart',item['name'])
    def remove_from_cart(self, item):
        # if product in self.items:
        #     self.items.remove(product)
        # else:
        #     print('Product None In Cart')
        self.items.pop(item - 1)
        return True
    def view_cart(self):
        i = 1
        for p in self.items:
            print(i,"Name :", p['name'], "Price : ", p['price'],"Quantity : ", p['quantity'])
            i += 1
    def place_order(self):
        totalPrice = 0
        for product in self.items:
            if product.get_quantity == 0:
                print(f"Sorry,{product.get_name()}is out of stock")
            else:
                totalPrice += product.get_price()
                product.update_quantity(0)
        self.items = []
        print(f'Order placed! Amount Price : {totalPrice}')
product1 = Electronics("Vivo Y11",66,5,12)
product2 = Electronics("Redmi Note 10s",80,5,12)
product3 = Clothing("Gaun Kondangan",90,5,2)
product4 = Book("Boku No Hero Academia",100,5,"Chandra")

cart = Cart()