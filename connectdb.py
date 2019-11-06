import pymysql
conn=pymysql.connect(host="localhost",db="sept",user="root")

mycursor = conn.cursor()

que="insert into login (username,pass) values('rm','22');"
mycursor.execute(que)
print("data inserted")

'''
que1="update login set pass='tum' where username='Ram';"
mycursor.execute(que1)
print("data updated")

que="delete from login where username='Ram';"
mycursor.execute(que)
print("data deleted")

que="""create table student_info2 
    (id int(3) primary key,name varchar(33),age int(3));
    """'''
mycursor.execute(que)
print("data inserted")
conn.commit()
conn.close()