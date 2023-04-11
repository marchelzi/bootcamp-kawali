from data_store import write_file, read_file

def cekUser(users, username):
    for u in users:
        if u['username'] == username:
            return False
    return True

def cekTujuan(account, tujuan):
    for a in range(len(account)):
        if account[a]['username'] == tujuan:
            return True
    return False

def cekSaldo(account, username):
    for a in account:
        if a['username'] == username:
            print('Saldo kamu : Rp. ', str(a['amount']))

def tarikTunai(account, transaction, username):
    amount = input('Masukkan nominal penarikan : ')
    for a in range(len(account)):
        if account[a]['username'] == username:
            if account[a]['amount'] - int(amount) >= 0:
                account[a]['amount'] -= int(amount)
                write_file("account.txt", account)
                transaction.append(
                    {
                        'username': username,
                        'to': 'self',
                        'amount': int(amount),
                        'type': 'withdraw'
                    }
                )
                write_file("transaksi.txt", transaction)
                print('Tarik tunai berhasil!')
            else:
                print('Maaf, saldo kamu tidak cukup!')

def setorTunai(account, transaction, username):
    amount = input('Masukkan nominal setor: ')
    for a in range(len(account)):
        if account[a]['username'] == username:
            account[a]['amount'] += int(amount)
            write_file("account.txt", account)
            transaction.append(
                {
                    'username': username,
                    'to': 'self',
                    'amount': int(amount),
                    'type': 'deposit' 
                }
            )
            write_file("transaksi.txt", transaction)
            print('Saldo anda berhasil di tambahkan!')
            

def transfer(account, transaction, username):
    amount = input('Masukkan jumlah transfer : ')
    while True:
        tujuan = input('Masukkan nama tujuan: ')
        if cekTujuan(account, tujuan):
            for a in range(len(account)):
                if account[a]['amount'] - int(amount) >= 0:
                    account[a]['amount'] -= int(amount)
                    for a in range(len(account)):
                        if account[a]['username'] == tujuan:
                            account[a]['amount'] += int(amount)
                            write_file("account.txt", account)
                            transaction.append(
                                {
                                    'username':username,
                                    'to': tujuan,
                                    'amount': int(amount),
                                    'type': 'transfer',
                                }
                            )
                            write_file("transaksi.txt", transaction)
                            print('Transfer berhasil!')
                            return True
                        
                else:
                    print('Nama tujuan tidak tesedia!')

def lihatTransaksi(transaction, username):
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


