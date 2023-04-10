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
            print('Your Balance : Rp. ', str(a['amount']))

def withdraw(account, transaction, username):
    amount = input('Masukkan nominal penarikan : ')
    for a in range(len(account)):
        if account[a]['username'] == username:
            if account[a]['amount'] - int(amount) >= 0:
                account[a]['amount'] -= int(amount)
                transaction.append(
                    {
                        'username':username,
                        'to': 'self',
                        'amount': int(amount),
                        'type': 'deposit'
                    }
                )
                print('Tarik tunai berhasil!')
            else:
                print('maaf, Saldo kamu tidak cukup!')

def deposit (account, transaction, username):
    amount = input('masukkan jumlah seposit : ')
    for a in range(len(account)):
        if account[a]['username'] == username:
            account[a]['amount'] += int(amount)
            transaction.append(
                {
                    'username' : username,
                    'to': 'self',
                    'amount': int(amount),
                    'type': 'deposit',
                }
            )
            print('Saldo berhasil di tambahkan!')

def transfer(account, transaction, username):
    amount = input('Masukkan jumlah transfer: ')
    while True:
        to = input('Masukkan nama tujuan: ')
        if cekTo(account, to):
            for a in range(len(account)):
                if account[a]['username'] == username:
                    if account[a]['amount'] - int(amount) >= 0:
                        account[a]['amount'] -= int(amount)
                        for a in range(len(account)):
                            if account[a]['username'] == to:
                                account[a]['amount'] += int(amount)
                                transaction.append(
                                    {
                                    'username' : username,
                                    'to': 'self',
                                    'amount': int(amount),
                                    'type': 'transfer'
                                    }
                                )
                                print('Tranfer berhasil!')
                                return True
                    else:
                        print('Saldo kmau tidak cukup!')
                        return False
        else:
            print('Nama tujuan tidak tersedia!')


def showTransaction(transaction, username):
    for t in range(len(transaction)):
        if transaction[t]['username'] == username:
            i = 1
            for t in range(len(transaction)):
                if transaction[t]['username'] == username:
                    print('')
                    print('=== Transaksi ', str(i), '===')
                    print('username : ', transaction[t]['username'])
                    print('to : ', transaction[t]['to'])
                    print('amount : ', transaction[t]['amount'])
                    print('type : ', transaction[t]['type'])
                    print('')
                i += 1
            return True
    print('Kamu belum melakukan transaksi apapun!')