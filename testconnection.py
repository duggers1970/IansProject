import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CupWinners20",
    database="sql_hr"
)

mycursor=mydb.cursor()

sqlformula = "insert into employees VALUES (%s,%s,%s,%s,%s,%s,%s)"
employees=[(115363,"McGrath","Paul","Assistant",10000,37270,10),
           (115359,"Brand","Lucas","Integrator",10000,37270,10),
           (115360,"Khan","Ruks","Secretary",10000,37270,10),
           (115361,"Else","Someone","Bossman",10000,37270,10),
           (115362,"Little","Stuart","Little Fella",10000,37270,10)]

mycursor.executemany(sqlformula,employees)

mydb.commit()

mycursor.execute("select * from employees")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)