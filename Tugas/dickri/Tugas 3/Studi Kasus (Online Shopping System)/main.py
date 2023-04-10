from data import cart,product1,product2,product3,product4

print("1. ", product1.get_name(), "Harga: ",product1.get_price(), "Kuantiti: ", product1.get_quantity(), "Priode: ", product1.get_warranty_period())
print("2. ", product2.get_name(), "Harga: ",product2.get_price(), "Kuantiti: ", product2.get_quantity(), "Priode: ", product2.get_warranty_period())
print("3. ", product3.get_name(), "Harga: ",product3.get_price(), "Kuantiti: ", product3.get_quantity(), "Priode: ", product3.get_size())
print("4. ", product4.get_name(), "Harga: ",product4.get_price(), "Kuantiti: ", product4.get_quantity(), "Priode: ", product4.get_author())

while True:
    pilihan = input('Masukan Nomor Produk Untuk Ditambahkan Kedalam Keranjang Anda (0 untuk keluar): ')
    if pilihan == '1':
        pdt_1 = {
            'name': product1.get_name(),
            'price': product1.get_price(),
            'quantity': 1
        }
        if product1.update_quantity(1):
            cart.add_to_cart(pdt_1)
    elif pilihan == '2':
        pdt_2 = {
            'name': product2.get_name(),
            'price': product2.get_price(),
            'quantity': 1
        }
        if product2.update_quantity(1):
            cart.add_to_cart(pdt_2)
    elif pilihan == '3':
        pdt_3 = {
            'name': product3.get_name(),
            'price': product3.get_price(),
            'quantity': 1
        }
        if product3.update_quantity(1):
            cart.add_to_cart(pdt_3)
    elif pilihan == '3':
        pdt_4 = {
            'name': product4.get_name(),
            'price': product4.get_price(),
            'quantity': 1
        }
        if product4.update_quantity(1):
            cart.add_to_cart(pdt_4)

    elif pilihan == '0':
        if len(cart.item) > 0:
            while True:
                cart.view_cart()
                print("")
                pilih = input('Masukan 1 Untuk Order, 2 Untuk Hapus Produk, atau 0 Untuk Exit: ')
                print("")
                if pilih == '1':
                    cart.place_order()
                    exit()
                elif pilih == '2':
                    cart.view_cart()
                    pilih == input('Masukan Nomor Produk Yang Dihapus: ')
                    print("")
                    for i in cart.item:
                        if i['name'] == product1.get_name():
                            product1.quantity += cart.item[int(pilihan)-1]['quantity']
                        elif i['name'] == product2.get_name():
                            product2.quantity += cart.item[int(pilihan)-1]['quantity']
                        elif i['name'] == product3.get_name():
                            product3.quantity += cart.item[int(pilihan)-1]['quantity']
                        elif i['name'] == product4.get_name():
                            product4.quantity += cart.item[int(pilihan)-1]['quantity']
                    cart.remove_from_cart(int(pilihan))
                elif pilih == 0:
                    exit()
        else:
            exit()
        