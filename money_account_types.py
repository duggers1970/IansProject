import config


def get_account_types():
    mycursor=config.mydb.cursor()
    mycursor.execute("select * from account_types")
    myresult=mycursor.fetchall()
    return myresult

def list_account_types():
    myresult=get_account_types()
    for row in myresult:
        print(row)

myresult=get_account_types()
list_account_types()

if(not myresult):
    duplicate=0

acc_type = input("Enter your account type: ")
acc_ob = input("Enter Opening Balance For " + acc_type + " ")

for row in myresult:
    if(acc_type==row[1]):
        duplicate=1
    else:
        duplicate=0

if(duplicate==1):
    print("Account Type " + acc_type + " is already saved.")
else:
    sqlformula = "insert into account_types (account_type_description, account_type_opening_balance) VALUES (%s,%s)"
    acc_type_record = [(acc_type),acc_ob]
    mycursor = config.mydb.cursor()
    mycursor.execute(sqlformula, acc_type_record)
    config.mydb.commit()


list_account_types()