from admin import addUser, deleteUser, showUser, showAllTransaction
from customer import showBalance, withdraw, deposit, transfer, showTransaction
from file_ops import write_to_file,read_file
users = read_file("users.txt")

cUser = {}

transaksi = read_file("transaksi.txt")
transaction = []

account = read_file("account.txt")


# User yang sedang login
def login(username, password, cUser):
    for u in users:
        if u['username'] == username and u['password'] == password:
            cUser.update(u)
            return True
    return False


# Proses Login
def login_process(cUser):
    while True:
        username = input('Username : ')
        passsword = input('Password : ')
        if login(username, passsword, cUser):
            print('Login Berhasil')
            break
        else:
            print('Login Gagal')

def menu(cUser):
    # Menu admin
    if cUser['role'] == 'admin':
        while True:
            print('== Menu ==')
            print('1. Add User')
            print('2. Delete User')
            print('3. Show Users')
            print('4. Show Transaction')
            print('5. Logout')
            choice = input('Choice : ')
            if choice == '1':
                addUser(users, account)
            elif choice == '2':
                deleteUser(users, account,transaction)
            elif choice == '3':
                showUser(users)
            elif choice == '4':
                showAllTransaction(transaction)
            elif choice == '5':
                cUser.clear()
                break
    # Menu customer
    elif cUser['role'] == 'customer':
        while True:
            print('== Menu ==')
            print('1. Show Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Transfer')
            print('5. Show Transaction')
            print('6. Logout')
            choice = input('Choice : ')
            if choice == '1':
                showBalance(account, cUser['username'])
            elif choice == '2':
                withdraw(account, transaction, cUser['username'])
            elif choice == '3':
                deposit(account, transaction, cUser['username'])
            elif choice == '4':
                transfer(account, transaction, cUser['username'])
            elif choice == '5':
                showTransaction(transaction, cUser['username'])
            elif choice == '6':
                cUser.clear()
                break

# Menu login
def main():
    while True:
        print('1. Login')
        print('2. Exit')
        choice = input('Choice: ')
        if choice == '1':
            login_process(cUser)
            menu(cUser)
        elif choice == '2':
            break
        print('\033c', end='')

main()
