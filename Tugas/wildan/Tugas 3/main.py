from product import Surga_Dan_Neraka, Sepatu_Compass, TV_Samsung
from chart import chart

def main():

    data = {}

    print('WELCOME TO OUR ONLINE SHOP SYSTEM')
    print('_________________________________')
    print()
    print('Available Product :')
    print('===================')

    print(f"1. {Surga_Dan_Neraka.name} (Book) - Price Rp.{Surga_Dan_Neraka.price}, Quantity: {Surga_Dan_Neraka.quantity}, Author Is {Surga_Dan_Neraka.auothor}")
    print(f"2. {Sepatu_Compass.name} (Clothing) - Price Rp.{Sepatu_Compass.price}, Quantity: {Sepatu_Compass.quantity}, Size Is {Sepatu_Compass.size}")
    print(f"3. {TV_Samsung.name} (Electronics) - Price Rp.{TV_Samsung.price}, Quantity: {TV_Samsung.quantity}, warranty period: {TV_Samsung.warranty_period} months" )
    print()
    choise = input("Input the number for add produtc to chart (or 0 for exit to chart)")

    if choise == '1':
        data.update({
            "name" :Surga_Dan_Neraka.getName(),
            "price" :Surga_Dan_Neraka.getPrice(),
            "quantity" :Surga_Dan_Neraka.getQuantity(),
        })
        chart.addToChart(data)

        Surga_Dan_Neraka.updateQuantity(-1)

    elif choise == '2':
        data.update({
                "name" :Sepatu_Compass.getName(),
                "price" :Sepatu_Compass.getPrice(),
                "quantity" :Sepatu_Compass.getQuantity(),
        })
        chart.addToChart(data)
        Sepatu_Compass.updateQuantity(-1)
    elif choise == '3' :
        data.update({
                "name" :TV_Samsung.getName(),
                "price" :TV_Samsung.getPrice(),
                "quantity" :TV_Samsung.getQuantity(),
        })
        TV_Samsung.updateQuantity(-1)
        chart.addToChart(data)   

    elif choise == "0":
        return False
    else:
        print('Not Validate input')

def chartS():
    print('CHART :')
    print('=======')
    chart.viewChart()
    print()
    choice = input('enter 1 to place order, 2 to remove product, or 0 to exit :')
    if choice == '1':
        chart.placeOrder()

    elif choice == '2':
        product = input('enter the number of product : ')
        produtc2 = chart.removeFromChart(product)
        if produtc2['name'] == "Surga_Dan_Neraka":
            Surga_Dan_Neraka.updateQuantity(produtc2['quantity'])
        elif produtc2['name'] == "Sepatu_Compass":
            Sepatu_Compass.updateQuantity(produtc2['quantity'])
        elif produtc2['name'] == "TV_Samsung":
            TV_Samsung.updateQuantity(produtc2['quantity'])

    elif choice == '0':
        return False
    else:
        print('not validate input')



while True:
    kondisi = main()
    if kondisi == False:
        break
while True:
    kondisi = chartS()
    if kondisi == False:
        break

    
    

