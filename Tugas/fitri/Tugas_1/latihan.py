class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.pintu = "tertutup"
        self.mobil = "mati"

    def membukaPintu(self):
        if self.pintu == 'tertutup':
            print('Pintu berhasil dibuka!')
            self.pintu = 'terbuka'
        else:
            print('Pintu telah terbuka!')

    def menutupPintu(self):
        if self.pintu == 'terbuka':
            print('Pintu berhasil ditutup!')
            self.pintu = 'tertutup'
        else:
            print('Pintu telah terbuka!')

    def menyalakanMobil(self):
        if self.mobil == 'mati':
            print('Mobil berhasil dinyalakan!')
            self.mobil = 'menyala'
        else:
            print('Mobil sudah menyala!')

    def mematikanMobil(self):
        if self.mobil == 'menyala':
            print('Mobil berhasil dimatikan!')
            self.mobil = 'mati'
        else:
            print('Mobil sudah mati!')

mobilku = car("toyota", 2023)

mobilku.membukaPintu()
mobilku.membukaPintu()
mobilku.membukaPintu()
mobilku.menutupPintu()
mobilku.menutupPintu()
mobilku.menutupPintu()
mobilku.menyalakanMobil()
mobilku.menyalakanMobil()
mobilku.menyalakanMobil()
mobilku.mematikanMobil()
mobilku.mematikanMobil()
mobilku.mematikanMobil()