import json, copy
_USER_FILE = './users.txt'
_ACCOUNT_FILE = './accounts.txt'
_TRANSACTION_FILE = './transaction.txt'
def write_to_file(file, data):
    json_string = json.dumps(data)

    f = open(file, 'w')
    f.write(json_string)
    f.close()

def read_file(file, mode='r'):
    try:
        f = open(file, mode=mode)
        json_string = f.read()
        json_dict = json.loads(json_string)
        f.close()
        return json_dict
    except:
        return False
    
cekUser = read_file(_USER_FILE)
accounts = read_file(_ACCOUNT_FILE)
current_users = {}
transactions = read_file(_TRANSACTION_FILE)
def check_user(cekUser, email):
    for user in cekUser:
        if user['email'] == email:
            return False
    return True
def add_users(users, current_users):
    print("===========================================")
    print("                  Add Users                ")
    email = input("\nAdd Email: ")
    password = input("Add password: ")
    print("1. Admin or 2. User")
    role = input("Enter Role: ")
    for user in users:
        if user['email'] == email:
            print("Email already exists")
            return True
        else:
            if role == '1':
                role = 'admin'
                break
            elif role == '2':
                role = 'user'
                break
        print("Enter role 1 or 2!")
        break
    if check_user(users, email):
        accounts.append({
            'email' : email,
            'amount' : 0
        }),  
        write_to_file(_ACCOUNT_FILE, accounts)
        users.append({
            'email': email,
            'password': password,
            'role': role
            })
        print("\n        User added successfully          ")
        write_to_file(_USER_FILE, users)
        print("===========================================")
        return True
    print("===========================================")

def delete_users(users, account, transaction):
    print("===========================================")
    print("                Data Users                 ")
    for user in users:
        print("\nEmail", user["email"], "    ||    ", "Role", user['role'])
    print("===========================================")
    
    while True:
        choice_del = input("Enter the email to delete: ")
        for user in users:
            for acc in account:
                trans = copy.copy(transaction)
                for tran in trans:
                    if user['email'] == choice_del and acc['email'] == choice_del and tran['email'] == choice_del:
                        users.remove(user)
                        account.remove(acc) 
                        transaction.remove(tran)
                        write_to_file(_USER_FILE, users)
                        write_to_file(_ACCOUNT_FILE, accounts)
                        write_to_file(_TRANSACTION_FILE, transaction)
                        print("           Delete successfully!          ")
                        print("===========================================")
                        return True
        print("Email not found!")
        print("===========================================")


def show_users(users):
    print("===========================================")
    print("                Data Users                 ")
    for user in users:
        print("\nEmail", user["email"], "    ||    ", "Role", user['role'])
    print("===========================================")

def show_transactions():
    print("===========================================")
    print("            Transaction data               ")
    for trans in range(len(transactions)):
        print(trans+1,"\nEmail: " , transactions[trans]['email'])
        print("","Destination: " , transactions[trans]['destination'])
        print("","Amount: " , transactions[trans]['amount'])
        print("","Type: " , transactions[trans]['type'])
        print("-------------------------------------------")
    print("\n          No transactions yet!")
    print("===========================================")

