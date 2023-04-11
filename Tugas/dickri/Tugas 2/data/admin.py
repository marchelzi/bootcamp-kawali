import json

def cekUser(users, user):
    for u in users:
        if u['user'] == user :
            return False
    return True
        
def tambahUser(users, account):
    while True:
        user = input('User : ')
        password = input('Password : ')

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
            account.append({
                'user' : user,
                'amount' : 0,
            })
            print('User berhasil di tambahkan!')
            return True
        else:
            json_users = json.dumps(users)
            data_users = open("data/users.txt", "w")
            data_users.write(json_users)
            data_users.close()
            print("Data Berhasil Dtambahkan")

def hapusUser(users, account):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['user'], ' (',users[u]['role'],')')
    
    while True:
        user = input('Masukan nama user yang mau di hapus : ')
        for u in range(len(users)):
            if users[u]['user'] == user:
                users.pop(u)
                account.pop(u)
                json_users = json.dumps(users)
                data_users = open("data/users.txt", "w")
                data_users.write(json_users)
                data_users.close()
                print("Data Berhasil Dtambahkan")
                print('User berhasil dihapus!')
                return True
        print('Pilih user yang ada!')

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



