from file_ops import write_to_file, read_file

def cekUser(users, username):
    for u in users:
        if u['username'] == username :
            return False
    return True

def cekTo(account, to):
    for a in range(len(account)):
        if account[a]['username'] == to:
            return True
    return False



def showBalance(account, username):
    for a in account:
        if a['username'] == username:
            print('Your Balance : ', str(a['amount']))

def withdraw(account, transaction, username):
    amount = input('Masukkan jumlah withdraw : ')
    for a in range(len(account)):
        if account[a]['username'] == username:
            if account[a]['amount'] - int(amount) >= 0:
                account[a]['amount'] -= int(amount)
                write_to_file('accounts.txt', account)
                transaction.append(
                    {
                        'username':username,
                        'to': 'self',
                        'amount': int(amount),
                        'type': 'Tarik Tunai',
                    }
                )
                write_to_file('transactions.txt', transaction)
                print('Tarik Tunai Berhasil')

            else:
                print('Maaf, Saldo kamu tidak cukup!')

def deposit(account, transaction, username):
    amount = input('Masukkan jumlah deposit : ')
    for a in range(len(account)):
        if account[a]['username'] == username:
            account[a]['amount'] += int(amount)
            write_to_file('accounts.txt', account)
            transaction.append(
                {
                    'username':username,
                    'to': 'self',
                    'amount': int(amount),
                    'type': 'deposit',
                }
            )
            write_to_file('transactions.txt', transaction)
            print('Saldo berhasil di tambahkan!')

def transfer(account, transaction, username):
    amount = input('Masukkan jumlah transfer : ')
    while True:
        to = input('Masukkan nama tujuan : ')
        if cekTo(account, to):
            for a in range(len(account)):
                if account[a]['username'] == username:
                    if account[a]['amount'] - int(amount) >= 0:
                        account[a]['amount'] -= int(amount)
                        for a in range(len(account)):
                            if account[a]['username'] == to:
                                account[a]['amount'] += int(amount)
                                write_to_file('accounts.txt', account)
                                transaction.append(
                                    {
                                        'username':username,
                                        'to': to,
                                        'amount': int(amount),
                                        'type': 'transfer',
                                    }
                                )
                                write_to_file('transactions.txt', transaction)
                                print('Transfer berhasil!')
                                return True
                    else:
                        print('Saldo kamu tidak cukup!')
                        return False
        else:
            print('Nama tujuan tidak tersedia!')
                
             
def showTransaction(transaction, username):
    for t in range(len(transaction)):
        if transaction[t]['username'] == username:
            print('username : ', transaction[t]['username'])
            print('to : ', transaction[t]['to'])
            print('amount : ', transaction[t]['amount'])
            print('type : ', transaction[t]['type'])
            print('')