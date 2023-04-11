from admin import addUser, deleteUser, showUser, showAllTransaction
from customer import cekSaldo, tarikTunai, setorTunai, transfer, lihatTransaksi
from data_store import write_file, read_file

users = read_file("pengguna.txt")
cUser = {}
transaction = read_file("transaksi.txt")

account = read_file("account.txt")


#
def infoLogin(username, password, cUser):
    for u in users:
        if u['username'] == username and u['password'] == password:
            cUser.update(u)
            return True
    return False


#
def login(cUser):
    while True:
        user = input('Username : ')
        password = input('Password : ')
        if infoLogin(user, password, cUser):
            print('Login Berhasil!')
            break
        else:
            print('Login gagal!')

def menu(cUser):
    #
    if cUser['role'] == 'admin':
        while True:
            print('== Menu ==')
            print('1. Tambah User')
            print('2. Hapus User')
            print('3. Lihat Users')
            print('4. Lihat Transaksi')
            print('5. Logout')
            pilihan = input('Pilih menu : ')
            if pilihan == '1':
                addUser(users, account)
            elif pilihan == '2':
                deleteUser(users, account, transaction)
            elif pilihan == '3':
                showUser(users)
            elif pilihan == '4':
                showAllTransaction(transaction)
            elif pilihan == '5':
                cUser.clear()
                break
    # Menu customer
    elif cUser['role'] == 'customer':
        while True:
            print('== Menu ==')
            print('1. Lihat Saldo')
            print('2. Tarik Tunai')
            print('3. Setor Tunai')
            print('4. Transfer')
            print('5. Lihat Transaksi')
            print('6. Logout')
            pilihan = input('Pilih Menu : ')
            if pilihan == '1':
                cekSaldo(account, cUser['username'])
            elif pilihan == '2':
                tarikTunai(account, transaction, cUser['username'])
            elif pilihan == '3':
                setorTunai(account, transaction, cUser['username'])
            elif pilihan == '4':
                transfer(account, transaction, cUser['username'])
            elif pilihan == '5':
                lihatTransaksi(transaction, cUser['username'])
            elif pilihan == '6':
                cUser.clear()
                break

# Menu login
def main():
    while True:
        print('1. Login')
        print('2. Exit')
        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            login(cUser)
            menu(cUser)
        elif pilihan == '2':
            break
        print('\033c', end='')

main()