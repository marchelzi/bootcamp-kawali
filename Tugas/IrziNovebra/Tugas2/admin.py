from file_ops import write_to_file, read_file
import copy

_USER_FILE = "users.txt"
_ACCOUNT_FILE = "account.txt"


def cekUser(users, username):
    for u in users:
        if u['username'] == username :
            return True
    return False
        
def addUser(users, account):
    while True:
        username = input('Username : ')
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
        
        if cekUser(users, username) == False:
            users.append({
                'username' : username,
                'password' : password,
                'role' : role
            })
            write_to_file(_USER_FILE,users),
            account.append({
                'username' : username,
                'amount' : 0,
            })
            print('User berhasil di tambahkan!')
            write_to_file(_ACCOUNT_FILE,account)
            return True
        else:
            print('Username sudah digunakan!')

def deleteUser(users, account,transaction):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], ' (',users[u]['role'],')')
    
    while True:
        choice = input('Masukan username user yang mau di hapus : ')
        for u in range(len(users)):
            for us in account:
                if users[u]['username'] == choice and us['username'] == choice:
                    users.pop(u)
                    account.remove(us)
                    write_to_file(_USER_FILE,users)
                    write_to_file(_ACCOUNT_FILE,account)
                    b = copy.copy(transaction)
                    for t in b:
                        if t['username'] == choice:
                            transaction.remove(t)
                            write_to_file('transaksi.txt',transaction)
                    print('User telah dihapus')
                    return True
        print('Pilih username yang ada!')

def showUser(users):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], ' (',users[u]['role'],')')

def showAllTransaction(transaction):
    for t in range(len(transaction)):
        print(str(t+1), '. ','username : ', transaction[t]['username'])
        print('   ', 'to : ', transaction[t]['to'])
        print('   ', 'amount : ', transaction[t]['amount'])
        print('   ', 'type : ', transaction[t]['type'])



