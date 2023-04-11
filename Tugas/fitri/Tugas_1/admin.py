def cekUser(users, username):
    for u in users:
        if u['username'] == username:
            return False
        return True

def addUser(users, account):
    while True:
        username = input('username : ')
        password = input('password : ')

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
            account.append({
                'username': username,
                'amount': 0,
            })
            print('User berhasil di tambahkan!')
            return True
        else:
            print('User name sudah digunakan!')

def deletUser(users, account):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], '(',users[u]['role'],')')

    while True:
        choice = input('Masukkan username user yang mau di hapus : ')
        for u in range(len(users)):
            if users[u]['username'] == choice:
                users.pop(u)
                account.pop(u)
                print('User removed')
                return True
        print('Pilih username yang ada!')
        
def showUsers(users):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], ' (',users[u]['role'],')')

def showAllTransaction(transaction):
    if len(transaction) > 0:
        for t in range(len(transaction)):
            print(str(t+1), '. ','user : ', transaction[t]['username'])
            print('   ', 'to : ', transaction[t]['to'])
            print('   ', 'amount : ', transaction[t]['amount'])
            print('   ', 'type : ', transaction[t]['type'])
    else:
        print('Belum ada transaksi yang di lakukan')