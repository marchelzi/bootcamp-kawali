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
            print('your balance : ', str(a['amount']))

def withdraw(account, transaction, username):
    amount = input('masukkan jumlah tarik tunai : ')
    for a in range(len(account)):
        if account[a]['username'] == username:
            if account[a]['amount'] - int(amount) >= 0:
                account[a]['amount'] -= int(amount)
                transaction.append(
                    {
                    'username':username,
                    'to': 'self',
                    'amount': int(amount),
                     'type': 'deposit',
                    }
                )
    for acc in account:
        print (acc)

def deposit(account, transaction, username):
    amount = input('masukkan jumlah deposit : ')
    for a in range(len(account)):
        if account[a]['username'] == 'username':
            account[a]['amount'] += int(amount)
            transaction.append(
            {
            'username':username,
            'to': 'self',
            'amount': int(amount),
            'type': 'deposit',
            }
    )
            print('saldo berhasil ditambahkan')

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
                                transaction.append(
                                    {
                                    'username' :username,
                                    'to' :to,
                                    'amount' :int(amount),
                                    'type' : 'tranfer',
                                    }
                                )
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
