import mysql.connector 

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    port=3306,
    database='anjali'
)
 
mycursor=mydb.cursor()
mycursor.execute('show databases')

for x in mycursor:
    print(x)

# mycursor.execute('create database anjali')
# mydb.commit()



# mycursor.execute('create table customers (name varchar(255),address varchar(255))')


# m="insert into customers(name,address)values('shiny','shiny villa')"
# mycursor.execute(m)
# mydb.commit()




sql='insert into customers (name,address) values (%s,%s)'
val=[
    ('nitha','lowstreet 4'),
    ('mithun','apple st 652'),
    ('gayatri','mountain 21'),
    ('aishu','main road 989'),
    ('anjith','sideway 1633')
    ]
mycursor.executemany(sql,val)
mydb.commit()






# import mysql.connector








# mydatabase=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     port=3306,
#     database='sooraj'
# )

# mycursor=mydatabase.cursor()
# mycursor.execute('show databases')
# # print(mycursor)
# # mycursor.execute('create database sooraj')
# # mydatabase.commit()
# for x in mycursor:
#     print(x)
