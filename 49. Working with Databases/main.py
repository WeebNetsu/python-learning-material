# python3 -m pip install mysql-connector-python
import mysql.connector as con  # to connect to mysql database

mydb = con.connect(  # connect to database
    host="localhost",
    user="netsu",
    password="root",
    database="python_example"
)

mycursor = mydb.cursor()
mycursor.execute("select * from tblUsers;")
# note: mydb.commit() to save all changes made to database
result = mycursor.fetchall()  # gets all returned results

for row in result:
    print(row)
