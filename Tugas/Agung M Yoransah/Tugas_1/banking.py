from user import addUser, deleteUser, showUser, showAllTransaction
from transactions import showBalance, withdraw, deposit, transfer, showTransaction
users = [
    {
        'username': 'agung@gmail.com',
        'password': '123',
        'role': 'admin'
    }
]

current_user = {}
transaction = []

account = [
    {
        'username':'agung@gmail.com',
        'amount': 0
    },
]


def login(username, password, current_user):
    for u in users:
        if u['username'] == username and u['password'] == password:
            current_user.update(u)
            return True
    return False


def login_process(current_user):
    while True:
        username = input('Username : ')
        passsword = input('Password : ')
        if login(username, passsword, current_user):
            print('Login Berhasil')
            break
        else:
            print('Login Gagal')

def menu(current_user):
    if current_user['role'] == 'admin':
        while True:
            print('Menu')
            print('1. Add User')
            print('2. Delete User')
            print('3. Show Users')
            print('4. Show Transaction')
            print('5. Logout')
            choice = input('Pilih : ')
            if choice == '1':
                addUser(users, account)
            elif choice == '2':
                deleteUser(users, account)
            elif choice == '3':
                showUser(users)
            elif choice == '4':
                showAllTransaction(transaction)
            elif choice == '5':
                current_user.clear()
                break
    elif current_user['role'] == 'customer':
        while True:
            print('Menu')
            print('1. Show Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Transfer')
            print('5. Show Transaction')
            print('6. Logout')
            choice = input('Pilih : ')
            if choice == '1':
                showBalance(account, current_user['username'])
            elif choice == '2':
                withdraw(account, transaction, current_user['username'])
            elif choice == '3':
                deposit(account, transaction, current_user['username'])
            elif choice == '4':
                transfer(account, transaction, current_user['username'])
            elif choice == '5':
                showTransaction(transaction, current_user['username'])
            elif choice == '6':
                current_user.clear()
                break

# Menu login
def main():
    while True:
        print('1. Login')
        print('2. Exit')
        choice = input('Choice: ')
        if choice == '1':
            login_process(current_user)
            menu(current_user)
        elif choice == '2':
            break
        print('\033c', end='')

main()
