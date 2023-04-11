from admin import write_to_file, read_file, _ACCOUNT_FILE

_TRANSACTION_FILE = './transaction.txt'

def check_user(users, email):
    for user in users:
        if user['email'] == email:
            return False
    return True

def check_transper(account, destination):
    for trans in range(len(account)):
        if account[trans]['email'] == destination:
            return True
    return False

def check_balance(account, email):
    for acc in account:
        if acc['email'] == email:
            print("Your balance: ", int(acc['amount']))

def withdraw(account, transaction, email):
    amount = int(input("Enter amount withdraw: "))

    for acc in range(len(account)):
        if account[acc]['email'] == email:
            if account[acc]['amount'] - amount >= 0:
                account[acc]['amount'] -= amount
                write_to_file(_ACCOUNT_FILE, account)
                transaction.append({
                    'email' : email,
                    'destination' : 'self',
                    'amount' : amount,
                    'type' : 'deposit'
                    
                })
                write_to_file(_TRANSACTION_FILE, transaction)
    print("Sorry, Your balance is insufficient!")

def deposit(account, transaction, email):
    amount = int(input("Enter amount deposit: "))

    for acc in range(len(account)):
        if account[acc]['email'] == email:
            account[acc]['amount'] += amount
            write_to_file(_ACCOUNT_FILE, account)
            transaction.append(
                {
                    'email' : email,
                    'destination' : 'self',
                    'amount' : amount,
                    'type' : 'deposit'
                }
                )
            write_to_file(_TRANSACTION_FILE, transaction)
    print("Balance added successfully!")

def transaction(account, transaction, email):
    amount = int(input("Enter the transaction amount: "))
    while True:
        t = input("Enter the destination email: ")
        if check_transper(account, t):
            for acc in range(len(account)):
                if account[acc]['email'] == email:
                    if account[acc]['amount'] - amount >= 0:
                        account[acc]['amount'] -= amount
                        for acc in range(len(account)):
                            if account[acc]['email'] == t:
                                account[acc]['amount'] += amount
                                write_to_file(_ACCOUNT_FILE, account)
                                transaction.append({
                                    'email' : email,
                                    'destination' : t,
                                    'amount' : amount,
                                    'type' :'transfer'

                                })
                                write_to_file(_TRANSACTION_FILE, transaction)
                                print("Transfer Successfully!")
                                return True
                    else:
                        print("Your balance is not enough!")
                        return True
        else:
            print("Destination email does not exist!")

def view_transaction(transactions, email):
    print("===========================================")
    print("            Transaction data               ")
    for trans in range(len(transactions)):
        if transactions[trans]['email'] == email:
            print(trans+1)
            print("Email: " , transactions[trans]['email'])
            print("Destination: " , transactions[trans]['destination'])
            print("Amount: " , transactions[trans]['amount'])
            print("Type: " , transactions[trans]['type'])
            print("-------------------------------------------")
        else:
            print("No transactions yet!")