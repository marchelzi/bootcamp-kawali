from index import  product1, product2, product3, product4, cart
def main():
    print("Welcome to Our Online Shopping System")
    print()
    print("Avaible Product:")
    print(f"1. Name: {product1.get_name()} - Price: ${product1.get_price()} - Quantity: {product1.get_quantity()} - Warranty Period: {product1.get_warranty_period()} months") 
    print(f"2. Name: {product2.get_name()} - Price: ${product2.get_price()} - Quantity: {product2.get_quantity()} - Warranty Period: {product2.get_warranty_period()} months") 
    print(f"3. Name: {product3.get_name()} - Price: ${product3.get_price()} - Quantity: {product3.get_quantity()} - Size: {product3.get_size()}") 
    print(f"4. Name: {product4.get_name()} - Price: ${product4.get_price()} - Quantity: {product4.get_quantity()} - Outhor: {product4.get_author()}") 

    while True:
        choise = int(input("Enter the product number to add to your cart (or 0 to exit) : "))
        if choise == 1:
            field = {
                'name': product1.get_name(),
                'price': product1.get_price(),
                'quantity': 1
            }
            if product1.update_quantity(1):
                cart.add_to_cart(field)
        elif choise == 2:
            field2 = {
                'name': product2.get_name(),
                'price': product2.get_price(),
                'quantity': 1
            }
            if product2.update_quantity(1):
                cart.add_to_cart(field2)
        elif choise == 3:
            field3 = {
                'name': product3.get_name(),
                'price': product3.get_price(),
                'quantity': 1
            }
            if product3.update_quantity(1):
                cart.add_to_cart(field3)
        elif choise == 4:
            field4 = {
                'name': product4.get_name(),
                'price': product4.get_price(),
                'quantity': 1
            }
            if product4.update_quantity(1):
                cart.add_to_cart(field4)
        elif choise == 0:
            while True:
                cart.view_cart()
                choise2 = int(input("Enter 1 to place order, 2 to remove product for cart, or 0 to exit: "))
                if choise2 == 0:
                    print("Thank you for shopping with us!")
                    break
                elif choise2 == 1:
                    cart.place_older()
                    break
                elif choise2 == 2:
                    cart.view_cart()
                    choise3 = int(input("Enter number product for delete: "))
                    cart.remove_from_cart(choise3)

                else:
                    print("Sorry, Input not Valid!")
            break
        else:
            print('Input Not Valid!')
    
main()
