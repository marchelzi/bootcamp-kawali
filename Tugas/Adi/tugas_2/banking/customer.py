from data_user import write_file

def cekUser(users, username):
    for u in users:
        if u['username'] == username:
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
            print('saldo kamu : ', str(a['amount']))

def withdraw(account, transaction, username):
    amount = input('masukkan jumlah tunai : ')
    for a in range(len(account)):
        if account[a]['username'] == username:
            if account[a]['amount'] - int(amount) >= 0:
                account[a]['amount'] -= int(amount)
                write_file('account.txt', account)
                transaction.append(
                    {
                    'username':username,
                    'to': 'self',
                    'amount': int(amount),
                     'type': 'deposit',
                    }
                )
                write_file('transaksi.txt', transaction)
    for acc in account:
        print (acc)

def deposit(account, transaction, username):
    amount = input('masukkan jumlah deposit : ')
    for a in range(len(account)):
        if account[a]['username'] == 'username':
            account[a]['amount'] += int(amount)
            write_file('account.txt', account)
            transaction.append(
            {
            'username':username,
            'to': 'self',
            'amount': int(amount),
            'type': 'deposit',
            }
    )
            print('saldo berhasil ditambahkan')
            write_file('transaksi.txt', transaction)
def transfer(account, transaction, username):
    amount = input('masukkan jumlah transfer : ')
    while True:
        to = input('masukkan nama tujuan : ')
        if cekTo(account, to):
            for a in range(len(account)):
                if account[a]['username'] == 'username':
                    if account[a]['amount'] - int(amount) >= 0:
                        account[a]['amount'] -= int(amount)
                        for a in range(len(account)):
                            if account[a]['username'] == to:
                                account[a]['amount'] += int(amount)
                                write_file('account.txt', account)
                                transaction.append(
                                    {
                                    'username' :username,
                                    'to' :to,
                                    'amount' :int(amount),
                                    'type' : 'tranfer',
                                    }
                                )
                                write_file('transaksi.txt', transaction)
                                print('tranfer berhasil')
                                return True
                    else:
                        print('saldo kamu tidak cukup!')
                        return False
            else: 
                print('nama tujuan tidak tersedia')
                

def showTransaction(transaction, username):
    for t in range(len(transaction)):
        if transaction[t]['username'] == username:
            print('username : ', transaction[t]['username'])
            print('to : ', transaction[t]['to'])
            print('amount : ', transaction[t]['amount'])
            print('type : ', transaction[t]['type'])
            print('')
