def cekUser(users, username):
    for u in users:
         if u['username'] == username:
             return False
    return True

def addUser(users, account):
    while True:
        username = input('username: ')
        password = input('password: ')
        role = input('Role (1: admin, 2: customer) :')

        if role == '1':
            role = 'admin'
        elif role == '2':
            role = 'customer'

            if cekUser(users, username):
                print('user berhasil di tambahkan!')
                users.append({
                    'username' : username,
                    'password' : password,
                    'role' : role
                })
                return True
            else:
                print('username sudah digunakan!')

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