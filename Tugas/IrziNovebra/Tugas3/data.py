#IRZI NOVEBRA
#FAJAR

from main import Product,Electronic,Book,Clothing,cart,product_1,product_2,product_3,product_4

# product_1 = Electronic('Samsung',7000000,15,1)

print("1.",product_1.get_name(),"- Harga:",product_1.get_price(),"- Kuantiti:",product_1.get_quantity(),"- Periode:",product_1.get_warraty_period())
print("2.",product_2.get_name(),"- Harga:",product_2.get_price(),"- Kuantiti:",product_2.get_quantity(),"- Periode:",product_2.get_warraty_period())
print("3.",product_3.get_name(),"- Harga:",product_3.get_price(),"- Kuantiti:",product_3.get_quantity(),"- Size:",product_3.get_size())
print("4.",product_4.get_name(),"- Harga:",product_4.get_price(),"- Kuantiti:",product_4.get_quantity(),"- Author:",product_4.get_author())

while True:
    pilihan = input('Masukkan Nomor Produk Untuk Ditambahkan Kedalam Keranjang Anda (0 Untuk Keluar) : ')
    if pilihan == '1':
        pdt_1 = {
            'name': product_1.get_name(),
            'price': product_1.get_price(),
            'quantity': 1
        }
        if product_1.update_quantity(1):
           cart.add_to_cart(pdt_1)
       

    elif pilihan == '2':
        pdt_2 = {
            'name': product_2.get_name(),
            'price': product_2.get_price(),
            'quantity': 1
        }
        if product_2.update_quantity(1):
           cart.add_to_cart(pdt_2)
     

    elif pilihan == '3':
        pdt_3 = {
            'name': product_3.get_name(),
            'price': product_3.get_name(),
            'quantity': 1
        }
        if product_3.update_quantity(1):
           cart.add_to_cart(pdt_3)

    elif pilihan == '4':
        pdt_4 = {
            'name': product_4.get_name(),
            'price': product_4.get_price(),
            'quantity': 1
        }
        if product_4.update_quantity(1):
           cart.add_to_cart(pdt_4)
       

    elif pilihan == '0':
        if len(cart.items) > 0:
            while True:
                cart.view_cart()
                print("")
                pilih = input('Masukan 1 Untuk Order, 2 Untuk Hapus, atau 0 Untuk Exit: ')
                print("")
                if pilih == '1':
                    cart.place_order()
                    exit()
                elif pilih == '2':
                    cart.view_cart()
                    pilih = input('Masukan Nomor Produk Yang Akan Dihapus: ')
                    print("")
                    for i in cart.items:
                        if i['name'] == product_1.get_name():
                            product_1.quantity += cart.items[int(pilihan)-1]['quantity']
                        elif i['name'] == product_2.get_name():
                            product_2.quantity += cart.items[int(pilihan)-1]['quantity']
                        elif i['name'] == product_3.get_name():
                            product_3.quantity += cart.items[int(pilihan)-1]['quantity']
                        elif i['name'] == product_4.get_name():
                            product_4.quantity += cart.items[int(pilihan)-1]['quantity']
                    cart.remove_from_cart(int(pilihan))
                elif pilih == 0:
                    exit()
        else:
            exit()

    

