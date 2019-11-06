import pymysql

try:
    conn = pymysql.connect(host="localhost", user="root", db="sept")
    mycursor = conn.cursor()
    print("connnection established")
    sql_select_Query = "select * from login where username='mohan'"

    mycursor.execute(sql_select_Query)
    #records = mycursor.fetchall()
    #records = mycursor.fetchmany(2)
    records = mycursor.fetchone()
    print(records)
    print("Total number of rows in login'table  is - ", mycursor.rowcount)
    print("Printing each row's column values i.e. login record")
    #for row in records:
        #print("username = ", row[0] )
        #print("password = ", row[1],"\n")
        #print(row)
    mycursor.close()

except ValueError as e:
    print("Error while connecting to MySQL", e)
finally:
   conn.close()
   print("MySQL connection is closed")