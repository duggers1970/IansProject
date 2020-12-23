import config


def get_transaction_types():
    mycursor=config.mydb.cursor()
    mycursor.execute("select * from transaction_types")
    myresult=mycursor.fetchall()
    return myresult

def list_transaction_types():
    myresult=get_transaction_types()
    for row in myresult:
        print(row)

myresult=get_transaction_types()
list_transaction_types()

if(not myresult):
    duplicate=0

trn_type = input("Enter your transaction type: ")


for row in myresult:
    if(trn_type==row[1]):
        duplicate=1
    else:
        duplicate=0

if(duplicate==1):
    print("Transaction Type " + trn_type + " is already saved.")
else:
    sqlformula = "insert into transaction_types (transaction_type_description) VALUES (%s)"
    trn_type_record = [trn_type]
    mycursor = config.mydb.cursor()
    mycursor.execute(sqlformula, trn_type_record)
    config.mydb.commit()


list_transaction_types()