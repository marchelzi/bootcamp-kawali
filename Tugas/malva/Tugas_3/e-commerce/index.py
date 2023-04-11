class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_name(self):
        return self.name
    def get_price(self):
        return float (self.price)
    def get_quantity(self):
        return self.quantity
    def update_quantity(self, quantity):
        if self.quantity - 1 < 0:
            print("Stock has exceeded the limit!")
            return False
        else:
            self.quantity -= quantity
            return True
class Electronics(Product):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, price, quantity)
        self.warrperiod = warranty_period

    def get_warranty_period(self):
        return self.warrperiod
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
        self.items = []
    def add_to_cart(self, item):
        for j in self.items:
            if j['name'] == item['name']:
                j['quantity'] += 1
                print(f"Product add to cart: {item['name']} ")
                return False
        self.items.append(item)
        print(f"Product add to cart: {item['name']} ")
    def remove_from_cart(self, item):
        for rfc in self.items:
            if rfc['name'] == product1.get_name():
                product1.quantity += self.items[(item) - 1]['quantity']
                self.items.pop(item - 1)
                return False
            elif rfc['name'] == product2.get_name():
                product2.quantity += self.items[(item) - 1]['quantity']
                self.items.pop(item - 1)
            elif rfc['name'] == product3.get_name():
                product3.quantity += self.items[(item) - 1]['quantity']
                self.items.pop(item - 1)
            elif rfc['name'] == product4.get_name():
                product4.quantity += self.items[(item) - 1]['quantity']
                self.items.pop(item - 1)
            else:
                print("Product None in cart!") 
    def view_cart(self):
        i = 1
        for vc in self.items:
            print(i, "Nama: ", vc['name'], "Price: ", vc['price'], "Quantity: ", vc['quantity'])
            i += 1
    def place_older(self):
        totalPrice = 0
        for po in self.items:
            totalPrice += (po['price'] * po['quantity'])
        print("Summary Order: ")
        print(f"Order placed! amount price: {totalPrice}")
        print("Thankyou For Order!")

product1 = Electronics("Vivo Y11",66.99, 5, 12)
product2 = Electronics("Redmi Note 10s Price",70, 5, 15)
product3 = Clothing("Jeans Cuyy", 20, 8, 7)
product4 = Book("Programing itu mudah",5, 9,"Malva")

cart = Cart()