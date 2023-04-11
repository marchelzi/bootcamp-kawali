class product:
    def __init__(self, name, prince, quantity):
        self.name = name
        self.prince = prince
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_prince(self):
        return float(self.prince)

    def get_quantity(self):
        return self.quantity

    def update_quantity(self, quantity):
        if self.quantity - 1 < 0:
            print('Barang sudah tidak tersedia')
            return False
        else:
            self.quantity -= 1
            return True

class electronics(product):
    def  __init__(self, name, prince, quantity, warranty_period):
        super().__init__(name, prince, quantity)
        self.warranty_period = warranty_period

    def get_warranty_period(self):
        return self.warranty_period

class clothing(product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size
        
    def get_size(self):
        return self.size

class book(product):
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
                print('Produk ditambahkankedalam keranjang')
                return True
        self.item.append(product)
        print ('Produk ditambahkan kedalam keranjang')
 
    def remove_from_cart(self, product):
        self.item.pop(product - 1)
        return True

    def view_cart(self):
        x = 1
        for i in self.item:
            print(x,".", i['name'], "Harga: ", i['price'], "Quantity: ", i['quantity'])
            x += 1
    def place_holder(self):
        jumlah = 0

        for i in self.item:
            jumlah += (i['price'] * i['quantity'])
            print('Ringkasan order: ', jumlah)
            print('Terimakasih telah berbelanja')


cart = Cart()

product_1 = electronics('Samsung Galaxy S9 (electronics)', 7000000, 15, 1)
product_2 = electronics('Xiaomi (electronics)', 6000000, 15, 2)
product_3 = clothing('Adidas Ultraboots Shoes (clothing)', 400000, 15, 8)
product_4 = book('The Catcher in the Rye (book)', 40000, 15, 'J.D. Saliger')