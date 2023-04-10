# main page
from product import Solo_Leveling, Iphone_XR, Sarung_GajahDuduk
from Chart import chart
def main():
    data = {}
    print(' -----Welcome To Our Online Shop System----- ')
    print('=============================================')
    print()
    print('Available Product : ')
    print()
    print(f"1. {Solo_Leveling.name} (book) - price Rp.{Solo_Leveling.price}, quantity:{Solo_Leveling.quantity} -- Author Is:{Solo_Leveling.author}")
    print(f"2. {Iphone_XR.name} (electronic) - price Rp.{Iphone_XR.price}, quantity:{Iphone_XR.quantity} -- Waarranty Period:{Iphone_XR.warranty_period}")
    print(f"3. {Sarung_GajahDuduk.name} (cloathing) - price Rp.{Sarung_GajahDuduk.price}, quantity:{Sarung_GajahDuduk.quantity} -- Size:{Sarung_GajahDuduk.size}")
    print()
    choise = input('Enter The Product Number For Add Product To Chart (or 0 for exit to chart): ')
    print()
    if choise == "1":
        data.update({
            "name" : Solo_Leveling.getName(),
            "price" : Solo_Leveling.getPrice(),
            "quantity" : 1
        })
        chart.addToChart(data)
        Solo_Leveling.updateQuantity(-1)
    elif choise == "2":
        data.update({
            "name" : Iphone_XR.getName(),
            "price" : Iphone_XR.getPrice(),
            "quantity" : 1
        })
        chart.addToChart(data)
        Iphone_XR.updateQuantity(-1)
    elif choise == "3":
        data.update({
            "name" : Sarung_GajahDuduk.getName(),
            "price" : Sarung_GajahDuduk.getPrice(),
            "quantity" : 1
        })
        chart.addToChart(data)
        Sarung_GajahDuduk.updateQuantity(-1)
    elif choise == "0":
        return False

    else:
        print("Not Validated Input")

def chartS():
    print("---Charts---")
    print("============")
    chart.viewChart()
    print()
    choice = input("Enter 1 to place order, 2 to remove product, or 0 to exit :")
    if choice == "1":
        chart.placeOrder()
    elif choice == "2":
        product = input("Enter the number of product : ")
        product2 = chart.removeFromChart(product)
        if product2 == "Solo Leveling":
            Solo_Leveling.updateQuantity(product2['quantity'])
        elif product2['name'] == "Iphone XR":
            Iphone_XR.updateQuantity(product2['quentity'])
        elif product2['name'] == "Sarung Gajah Duduk":
            Sarung_GajahDuduk.updateQuantity(product2['quentity'])
    elif choice == "0":
        return False
    else:
        print("Not Validated Input")


while True:
    kondisi = main()
    if kondisi == False:
        break

while True:
    kondisi = chartS()
    if kondisi == False:
        break