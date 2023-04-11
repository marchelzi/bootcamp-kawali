from data_store import write_file, read_file
import copy
def cekUser(users, username):
    for u in users:
        if u['username'] == username:
            return False
        return True

def addUser(users, account):
    while True:
        username = input('Username : ')
        if len(username) > 0 :
            while True:
                password = input('Password : ')
                if len(password) > 0 :
                    while True:
                        role = input('Role(1: Admin, 2: Customer) : ')
                        if role == '1':
                            role = 'admin'
                            break
                        elif role == '2':
                            role = 'customer'
                            break
                        print('Masukkan role yang sesuai!')

                    if cekUser(users, username):
                        users.append({
                            'username': username,
                            'password': password,
                            'role': role
                        }),
                        write_file("pengguna.txt", users)
                        account.append({
                            'username': username,
                            'amount': 0,
                        })
                        write_file('account.txt', account)
                        print('User berhasil di tambahkan!')
                        return True
                    else:
                        print('Nama user sudah digunakan!')
                else:
                    print('Harap masukan password!')
        else:
            print('Harap masukan nama user!')

def deleteUser(users, account, transaksi):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], '(',users[u]['role'],')')

    while True:
        choice = input('Masukkan username yang mau di hapus : ')
        for u in range(len(users)):
            for acc in account:
                if users[u]['username'] == choice and acc['username'] == choice:
                    users.pop(u)
                    account.remove(acc)
                    write_file("pengguna.txt", users)
                    write_file("account.txt", account)
                    trans = copy.copy(transaksi)
                    for tran in trans:
                        if tran["username"] == choice:
                            transaksi.remove(tran)
                            write_file('transaksi.txt', transaksi)
                            print('User removed')
                    return True
        print('Pilih user yang ada!')
        
def showUser(users):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], ' (',users[u]['role'],')')

def showAllTransaction(transaction):
    for t in range(len(transaction)):
        print(str(t+1), '. ','username: ', transaction[t]['username'])
        print('   ', 'to : ', transaction[t]['to'])
        print('   ', 'amount : ', transaction[t]['amount'])
        print('   ', 'type : ', transaction[t]['type'])
    print('Belum ada transaksi yang di lakukan')