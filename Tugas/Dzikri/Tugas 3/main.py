class Produk:
    def __init__(self, nama, harga, kuantitas):
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return float(self.harga)

    def get_kuantitas(self):
        return self.kuantitas

    def update_kuantitas(self):
        if self.kuantitas - 1 < 0:
            print('Barang sudah tidak tersedia')
            return False
        else:
            self.kuantitas -= 1
            return True

class Elektronik(Produk):
    def __init__(self, nama, harga, kuantitas, garansi):
        super().__init__(nama, harga, kuantitas)
        self.garansi = garansi
    
    def get_garansi(self):
        return self.garansi

class Pakaian(Produk):
    def __init__(self, nama, harga, kuantitas, ukuran):
        super().__init__(nama, harga, kuantitas)
        self.ukuran = ukuran

    def get_ukuran(self):
        return self.ukuran

class Buku(Produk):
    def __init__(self, nama, harga, kuantitas, penulis):
        super().__init__(nama, harga, kuantitas)
        self.penulis = penulis

    def get_penulis(self):
        return self.penulis

class Keranjang:
    def __init__(self):
        self.items = []
    def tambah_ke_keranjang(self, item):
        for i in self.items:
            if i['nama'] == item['nama']:
                i['kuantitas'] += 1
                print('Produk berhasil di tambahkan ke keranjang')
                return True
        self.items.append(item)
        print('Produk berhasil di tambahkan ke keranjang')

    def hapus_dari_keranjang(self, item):
            self.items.pop(item - 1 )
            return True

    def lihat_keranjang(self):
        x = 1
        for i in self.items:
            print(x, i['nama'], '- Harga: ', i['harga'], 'Kuantitas: ', i['kuantitas'] )
            x+=1

    def pemesanan(self):
        pass

produk1 = Elektronik('Samsung Galaxy S23 (Elektronik)', 20000000, 50, "6 Bulan")
produk2 = Pakaian('Cardinal T-Shirt', 100000, 30, "Xtra Large")
produk3 = Buku('Novel Jurnalisa', 250000, 3, "Lisa Product")
produk4 = Elektronik('Airpods', 2000000, 200, "3 Bulan")

keranjang = Keranjang()

print('Selamat datang di sistem belanja online')
print("1. ",produk1.get_nama(), "- Harga: Rp.", produk1.get_harga(), ", kuantitas: ", produk1.get_kuantitas(), ", Garansi: ", produk1.get_garansi())
print("2. ",produk2.get_nama(), "- Harga: Rp.", produk2.get_harga(), ", kuantitas: ", produk2.get_kuantitas(), ", Ukuran: ", produk2.get_ukuran())
print("3. ",produk3.get_nama(), "- Harga: Rp.", produk3.get_harga(), ", kuantitas: ", produk3.get_kuantitas(), ", Penulis: ", produk3.get_penulis())
print("4. ",produk4.get_nama(), "- Harga: Rp.", produk4.get_harga(), ", kuantitas: ", produk4.get_kuantitas(), ", Garansi: ", produk4.get_garansi())
while True:
    pilihan  = input('Masukkan nomor produk untuk menambahkan produk ke keranjang (atau 0 untuk keluar): ')
    if pilihan == '1':
        pk1 =   {
                    'nama': produk1.get_nama(), 
                    'harga': produk1.get_harga(),
                    'kuantitas' : 1
                }
        if produk1.update_kuantitas():
            keranjang.tambah_ke_keranjang(pk1)

    elif pilihan == '2':
        pk2 =   {
                    'nama': produk2.get_nama(), 
                    'harga': produk2.get_harga(),
                    'kuantitas' : 1
                }
        if produk2.update_kuantitas():
            keranjang.tambah_ke_keranjang(pk2)
    elif pilihan == '3':
        pk3 =   {
                    'nama': produk3.get_nama(), 
                    'harga': produk3.get_harga(),
                    'kuantitas' : 1
                }
        if produk3.update_kuantitas():
            keranjang.tambah_ke_keranjang(pk3)
    elif pilihan == '4':
        pk4 =   {
                    'nama': produk4.get_nama(), 
                    'harga': produk4.get_harga(),
                    'kuantitas' : 1
                }
        if produk4.update_kuantitas():
            keranjang.tambah_ke_keranjang(pk4)
    elif pilihan == '0':
        if len(keranjang.items) > 0:
            while True:
                keranjang.lihat_keranjang()
                pilihan = input('Masukkan 1 untuk order, 2 untuk hapus dari keranjang, 0 untuk keluar : ')
                if pilihan == '1':
                    jumlah = 0
                    for i in keranjang.items:
                        jumlah += (i['harga'] * i['kuantitas'])
                    print('Ringkasan pesanan:')
                    print('Total harga: ',jumlah)
                    print('Terima kasih telah berbelanja')
                    exit()
                elif pilihan == '2':
                    keranjang.lihat_keranjang()
                    pilihan = input('Masukkan nomor produk yang akan di hapus : ')
                    for i in keranjang.items:
                        if i['nama'] == produk1.get_nama():
                            produk1.kuantitas += keranjang.items[int(pilihan)-1]['kuantitas']
                        elif i['nama'] == produk2.get_nama():
                            produk2.kuantitas += keranjang.items[int(pilihan)-1]['kuantitas']
                        elif i['nama'] == produk1.get_nama():
                            produk3.kuantitas += keranjang.items[int(pilihan)-1]['kuantitas']
                        else:
                            produk4.kuantitas += keranjang.items[int(pilihan)-1]['kuantitas']
                    keranjang.hapus_dari_keranjang(int(pilihan))
                elif pilihan == '0':
                    exit()
        else:
            exit()