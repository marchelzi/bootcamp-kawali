from data_user import write_file

def cekUser(users, username):
    for u in users:
         if u['username'] == username:
             return False
    return True

def addUser(users, account):
    while True:
        username = input('username: ')
        if len(username) > 0:
            if cekUser(users, username):
                while True:
                    password = input('password: ')
                    if len(password) > 0:
                        while True:
                            role = input('Role (1: admin, 2: customer) :')
                            if role == '1':
                                    role = 'admin'
                                    break
                            elif role == '2':
                                    role = 'customer'
                                    break
                            print('masukkan role yang sesuai : ')
                        users.append({
                            'username' : username,
                            'password' : password,
                            'role' : role
                        }) 
                        write_file('user.txt', users)
                        account.append({
                            'username' : username,
                            'amount' : 0,
                        })
                        write_file('account', account)
                        print('user berhasil di tambahkan!')
                        return True
                    else:
                        print('harap masukkan password !')    
            else:
                print('username sudah digunakan!')
        else:
            print('harap masukkan username!')

def deleteTransaksi(transaction, username):
    import copy
    b = copy.copy(transaction)
    for item in b:
        if item['username'] == username:
            print(item)
            transaction.remove(item)
    write_file('transaksi.txt', transaction)
    return True

def deleteUser(users, account):
    print('daftar user : ')
    for u in range(len(users)):
        print(str(u+1), '.', users[u]['username'],'(', users[u]['role'],')')

    while True:
        choice = input('masukkan username user!')
        for u in users:
            if u['username'] == choice:
                users.remove(u)
                print('user removed')
                write_file('user.txt', users)
                write_file('account.txt', account)
                return True          
        print('pilih username yang ada!')

def showUser(user):
    print('daftar user')
    for u in range(len(user)):
        print(str(u+1)+'.' +user[u]['username']+ '('+user[u]['role']+')')

def showAllTransaction(transaction):
    for t in range(len(transaction)):
        print(str(t+1),'.','username : ', transaction[t]['username'])
        print('  ', 'to : ', transaction[t]['to'])
        print('  ', 'amount : ', transaction[t]['amount'])
        print('  ', 'type : ', transaction[t]['type'])
    else:
        print('belum ada transaksi yang digunakan')