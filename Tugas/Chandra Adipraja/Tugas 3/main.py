from index import Product,product1,product2,product3,product4,cart
def main():
    print("Welcome To Our Online Shopping System")
    print()
    print("Avaible Product:")
    print("1. Name :",product1.get_name(),",Price: $",product1.get_price(), ",Quantity:",product1.get_quantity(),",Warranty Period :",product1.get_warranty_period(),"Month")
    print("2. Name :",product2.get_name(),",Price: $",product2.get_price(), ",Quantity:",product2.get_quantity(),",Warranty Period :",product2.get_warranty_period(),"Month")
    print("3. Name :",product3.get_name(),",Price: $",product3.get_price(), ",Quantity:",product3.get_quantity(),",Size :",product3.get_size())
    print("4. Name :",product4.get_name(),",Price: $",product4.get_price(), ",Quantity:",product4.get_quantity(),",Author :",product4.get_author())
    while True:
        choise = int(input("Enter the product number to add to your cart ( or 0 to exit ) : "))
        if choise == 1:
            field = {
                'name' : product1.get_name(),
                'price' : product1.get_price(),
                'quantity' : 1
            }
            # cart.add_to_cart(field)
            # product1.update_quantity(1)
            if product1.update_quantity(1):
                cart.add_to_cart(field)
        elif choise == 2:
            field2 = {
                'name' : product2.get_name(),
                'price' : product2.get_price(),
                'quantity' : 1
            }
            # cart.add_to_cart(field2)
            # product2.update_quantity(1)
            if product2.update_quantity(1):
                cart.add_to_cart(field2)
        elif choise == 3:
            field3 = {
                'name' : product3.get_name(),
                'price' : product3.get_price(),
                'quantity' : 1
            }
            # cart.add_to_cart(field3)
            # product3.update_quantity(1)
            if product3.update_quantity(1):
                cart.add_to_cart(field3)
        elif choise == 4:
            field4 = {
                'name' : product4.get_name(),
                'price' : product4.get_price(),
                'quantity' : 1
            }
            # cart.add_to_cart(field4)
            # product4.update_quantity(1)
            if product4.update_quantity(1):
                cart.add_to_cart(field4)
        elif choise == 0:
            if len(cart.items) > 0:
                while True:
                    cart.view_cart()
                    choisee = int(input('Enter 1 For Order, 2 For Delete From Cart, 0 For Exit : '))
                    if choisee == 1:
                        jumlah = 0
                        for i in cart.items:
                            jumlah += (i['price'] * i['quantity'])
                        print('Summary Order : ')
                        print('Amount Price :$',jumlah)
                        print('Thankyou For Order!')
                        exit()
                    elif choisee == 2:
                        cart.view_cart()
                        choisee = input('Enter Number Product For Delete : ')
                        for i in cart.items:
                            if i['name'] == product1.get_name():
                                product1.quantity += cart.items[int(choisee) - 1]['quantity']
                            elif i['name'] == product2.get_name():
                                product2.quantity += cart.items[int(choisee) - 1]['quantity']
                            elif i['name'] == product3.get_name():
                                product3.quantity += cart.items[int(choisee) - 1]['quantity']
                            else :
                                product4.quantity += cart.items[int(choisee) - 1]['quantity']
                        cart.remove_from_cart(int(choisee))
                    elif choisee == 0:
                        exit()
            else:
                print("Thankyou For Coming")
                exit()
        else:
            print('Input Not Valid')
main()
