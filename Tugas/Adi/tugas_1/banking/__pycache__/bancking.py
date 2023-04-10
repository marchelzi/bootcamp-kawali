from users import addUser, deleteUser, showUser, showAllTransaction
from customer import showBalance, withdraw, deposit, transfer, showTransaction

users = [
    {
    'username' : 'z',
    'password' : '1',
    'role' : 'admin'
    },
    {
    'username' : 'a',
    'password' : '1',
    'role' : 'customer'
    }
]

#admin
cUser = {}

transaction = []

#customer
account = [
    {
    'username' : 'a',
    'amount' : 0
    }
]

#user yang sedang login
def login(username, password, cUser):
    for u in users:
        if u['username'] == username and u['password'] == password:
            cUser.update(u)
            return True
    return False

#proses login
def login_process(cUser):
    while True:
     username = input('username : ')
     password = input('password : ')
     if login(username, password, cUser):
        print('login succes')
        break 
    else:
        print('login failed')

def menu(cUser):
    #menu admin
    if cUser['role']  == 'admin':
        while True:
            print(cUser)
            print('1. tambah user')
            print('2. hapus user')
            print('3. tampilkan users')
            print('4. lihat transaksi')
            print('5. logout')
            choice = input('choice : ')
            if choice == '1':
                addUser(users, account) 
                print(users)
            elif choice == '2':
                deleteUser(users, account)
            elif choice == '3':
                showUser(users)
            elif choice == '4':
                showAllTransaction(transaction)
            elif choice == '5':
                break

#menu customer
    elif cUser['role'] == 'customer':
        while True:
            print('1. lihat saldo')
            print('2. tarik tunai')
            print('3. deposit')
            print('4. transfer')
            print('5. lihat transaksi')
            print('6. logout')
            choice = input('choice : ')
            if choice == '1':
                showBalance(account, cUser['username'])
            elif choice == '2':
                withdraw(account, transaction, cUser['username'])
            elif choice == '3':
                deposit(account, transaction, cUser['username'])
            elif choice == '4':
                transfer(account, transaction)
            elif choice == '5':
                showTransaction(transaction, cUser['username'])
            elif choice == '6':
                cUser.clear()
                break

#menu login
def main():
    while True:
        print('1. login')
        print('2. exit')
        choice = input('choice : ')
        if choice == '1':
            login_process(cUser)
            menu(cUser)
        elif choice == '2':
            break
        print('\033c', end='')

main()