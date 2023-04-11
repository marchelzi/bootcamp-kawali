def cekUser(users, username):
    for u in users:
        if u['username'] == username:
            return False
    return True
    

def addUser(users, account):
    while True:
        username = input('Username: ')
        password = input('Password: ')

        while True:
            role = input('Role (1: admin, 2: customer) :')
            if role == '1':
                role = 'admin'
                break
            elif role == '2':
                role = 'customer'
                break
            print('Masukan role yang sesuai!')

        if cekUser(users,username):
            users.append({
                'username': username,
                'password': password,
                'role': role
            }),
            account.append({
                'username': username,
                'amount': 0,
            })
            print('User successfully added!')
            return True
        else:
            print('Username is already in use!')

def deleteUser(users, account):
    print('Daftar User: ')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], '(',users[u]['role'], ')')

    while True:
        choice = input('Masukan username user yang ingin dihapus: ')
        for u in range(len(users)):
            if users[u]['username'] == choice:
                users.pop(u)
                account.pop(u)
                print('User removed')
                return True
            print('Pilih username yang ada!')

def showUser(users):
    print('Daftar user: ')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], '(',users[u]['role'],')')
    
def showAllTransaction(transaction):
    for t in range(len(transaction)):
        print(str(t+1), '. ', 'username: ', transaction[t]['username'])
        print('   ', 'to: ', transaction[t]['to'])
        print('   ', 'amount: ', transaction[t]['amount'])
        print('   ', 'type: ', transaction[t]['type'])
    else:
        print('No transactions have been made yet')