from data import writeFile, readFile

def cekUser(users, user):
    for u in users:
        if u['user'] == user :
            return False
    return True
        
def tambahUser(users, account):
    while True:
        user = input('User : ')
        if len(user) > 0:
            while True:
                password = input('Password : ')
                if len(password) > 0 :
                    while True:
                        role = input('Role (1: admin, 2: customer) :')
                        if role == '1':
                            role = 'admin'
                            break
                        elif role == '2':
                            role = 'customer'
                            break
                        print('Masukkan role yang sesuai!')
        
                    if cekUser(users, user):
                            users.append({
                                'user' : user,
                                'password' : password,
                                'role' : role
                            }),
                            writeFile('users.txt', users)
                            account.append({
                                'user' : user,
                                'amount' : 0,
                            })
                            writeFile('akun.txt', account)
                            print('User berhasil di tambahkan!')
                            return True
                    else:
                            print('Nama User sudah digunakan!')
                else:
                    print('Harap masukkan password')
        else:
            print('Harap masukkan nama user')

def hapusTransaksi(transaksi, user):
    import copy
    b = copy.copy(transaksi)
    for item in b:
        if item['user'] == user:
            print(item)
            transaksi.remove(item)
    writeFile('transaksi.txt', transaksi)
    return True

def hapusUser(users, account, transaksi):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['user'], ' (',users[u]['role'],')')
    
    while True:
        user = input('Masukan nama user yang mau di hapus : ')
        for u in range(len(users)):
            if users[u]['user'] == user:
                if hapusTransaksi(transaksi, user):
                    users.pop(u)
                    account.pop(u)
                    writeFile('users.txt', users)
                    writeFile('akun.txt', account)
                    print('User berhasil dihapus!')
                    return True
        print('Pilih User yang ada!')

def lihatUser(users):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['user'], ' (',users[u]['role'],')')

def lihatSemuaTransaksi(transaksi):
    if len(transaksi) > 0:
        for t in range(len(transaksi)):
            print(str(t+1), '. ','user : ', transaksi[t]['user'])
            print('   ', 'to : ', transaksi[t]['to'])
            print('   ', 'amount : ', transaksi[t]['amount'])
            print('   ', 'type : ', transaksi[t]['type'])
    else:
        print('Belum ada transaksi yang di lakukan')



