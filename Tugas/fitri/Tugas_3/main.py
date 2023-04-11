#Agung M.Y.
#Fitri N.F.
from data import product, electronics, clothing, book, Cart, cart, product_1, product_2, product_3, product_4

print("1. ", product_1.get_name(), ",  Harga: ", product_1.get_prince(), ",  Kuantiti: ", product_1.get_quantity(), ",  Periode: ", product_1.get_warranty_period())

print("2. ", product_2.get_name(), ",  Harga: ", product_2.get_prince(), ",  Kuantiti: ", product_2.get_quantity(), ",  Periode: ", product_2.get_warranty_period())

print("3. ", product_3.get_name(), ",  Harga: ", product_3.get_prince(), ",  Kuantiti: ", product_3.get_quantity(), ",  Periode: ", product_3.get_size())

print("4. ", product_4.get_name(), ",  Harga: ", product_4.get_prince(), ",  Kuantiti: ", product_4.get_quantity(), ",  Periode: ", product_4.get_author())

while True:
    pilihan = input('Masukkan nomor produk untuk ditambahkan ke keranjang anda! (0 untuk keluar): ')
    if pilihan == '1':
        pdt_1 = {
            'name': product_1.get_name(),
            'price': product_1.get_prince(),
            'quantity': 1
        }
        if product_1.update_quantity(1):
            cart.add_to_cart(pdt_1)

    elif pilihan == '2':
        pdt_2 = {
            'name': product_2.get_name(),
            'price': product_2.get_prince(),
            'quantity': 1
        }
        if product_2.update_quantity(1):
            cart.add_to_cart(pdt_2)

    elif pilihan == '3':
        pdt_3 = {
            'name': product_3.get_name(),
            'price': product_3.get_prince(),
            'quantity': 1
        }
        if product_3.update_quantity(1):
            cart.add_to_cart(pdt_3)

    elif pilihan == '4':
        pdt_4 = {
            'name': product_4.get_name(),
            'price': product_4.get_prince(),
            'quantity': 1
        }
        if product_4.update_quantity(1):
            cart.add_to_cart(pdt_4)

    elif pilihan == '0':
        if len (cart.item) > 0:
            while True:
                print("")
                cart.view_cart()
                pilih = input('Masukkan 1 untuk order, 2 untuk hapus produk, atau 0 untuk exit: ')
                print("")
                if pilih == '1':
                    cart.place_holder()
                    exit()
                elif pilih == '2':
                    cart.view_cart()
                    pilih = input('Masukkan nomor produk yang akan di hapus: ')
                    print("")
                    for i in cart.item:
                        if i['name'] == product_1.get_name():
                            product_1.quantity += cart.item[int(pilihan)-1]['quantity']
                        elif i['name'] == product_2.get_name():
                            product_2.quantity += cart.item[int(pilihan)-1]['quantity']
                        elif i['name'] == product_3.get_name():
                            product_3.quantity += cart.item[int(pilihan)-1]['quantity']
                        elif i['name'] == product_4.get_name():
                            product_4.quantity += cart.item[int(pilihan)-1]['quantity']
                    cart.remove_from_cart(int(pilihan))
                elif pilih == '0':
                    exit()
        else:
            exit()