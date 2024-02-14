# import mysql.connector 

# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     port=3306,
#     database='practice_session'
# )
 
# mycursor=mydb.cursor()
# mycursor.execute('create table fun (name varchar(12),rollno int)')

# p="insert into fun(name,rollno)values('anu',12)"
# mycursor.execute(p)
# mydb.commit()

# a="insert into fun(name,rollno)values(%s,%s)"
# v=[('mary',13),
#    ('leo',34)]

# b=mycursor.execute('delete from fun where rollno=34')
# c=mycursor.execute('update fun set rollno=23 where name="anu"')
# mydb.commit()

# mycursor.execute('select * from fun')
# result=mycursor.fetchall()
# print(result)
# print(type(result))
# for i in result:
#     for j in i:
#         print(j)

# mycursor.executemany(a,v)
# mydb.commit()


# mycursor.execute('create table customers (name varchar(255),address varchar(255))')


# m="insert into customers(name,address)values('shiny','shiny villa')"
# mycursor.execute(m)
# mydb.commit()

# sql='insert into customers (name,address) values (%s,%s)'
# val=[
#     ('nitha','lowstreet 4'),
#     ('mithun','apple st 652'),
#     ('gayatri','mountain 21'),
#     ('aishu','main road 989'),
#     ('anjith','sideway 1633')
#     ]
# mycursor.executemany(sql,val)
# mydb.commit()

# mycursor.execute('select * from customers')
# # myresult=mycursor.fetchone()
# myresult=mycursor.fetchall()

# print(myresult)
# print(type(myresult))


# for x in myresult:
#     print(x)
#     print(',,,,,,,,,,,,,,,,,')
    
