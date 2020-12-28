import config



def get_account_types():
    mycursor=config.mydb.cursor()
    mycursor.execute("select * from account_types")
    myresult=mycursor.fetchall()
    return myresult

def get_bank_accounts():
    mycursor=config.mydb.cursor()
    mycursor.execute("select * from bank_accounts")
    myresult=mycursor.fetchall()
    return myresult

def list_account_types():
    myresult=get_account_types()
    for row in myresult:
        print(row)

def list_bank_accounts():
    myresult=get_bank_accounts()
    for row in myresult:
        print(row)

myresult=get_account_types()
list_account_types()



acc_type = int(input("Enter the account type for your new account: "))

duplicate = 0
for account_type in myresult:
    print("Myresult",myresult)
    print("acc type", acc_type)
    print(type(acc_type))
    print("stored acc type:",account_type[0])
    print(type(account_type[0]))
    print("Stored account desc",account_type[1])
    if(acc_type==account_type[0]):
        print("dups")
        duplicate=1

print('Duplicate: ' ,duplicate)
if(duplicate==0):
    print("Account Type " + str(acc_type) + " is not a valid account")
else:
    acc_name = input("Enter the bank name of the new account: ")
    acc_sort_code = input("Enter the sort code of the new account: ")
    acc_account_number = input("Enter the account number of the new account: ")
    acc_balance = input("Enter the opening balance of the new account: ")
    sqlformula = "insert into bank_accounts (bank_account_type, bank_account_bank_name, bank_account_sort_code, bank_account_number, bank_account_balance) VALUES (%s,%s,%s,%s,%s)"
    bank_acc_record = [acc_type,acc_name,acc_sort_code,acc_account_number,acc_balance,]
    mycursor = config.mydb.cursor()
    mycursor.execute(sqlformula, bank_acc_record)
    config.mydb.commit()


list_bank_accounts()

