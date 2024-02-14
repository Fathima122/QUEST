#                                                         buildin methods in oops

#                                                              getattr()

# class Person:
#     name='john'
#     age=35
#     country='India'
# x=getattr(Person,'name1','not present')
# print(x)

# #                                                                delattr
# class Person:
#     name='john'
#     age=35
#     country='India'
# print(Person.age)
# x=getattr(Person,'age','not present')
# print(x)
# print(Person.name)
# # delattr(Person,'age')
# print(Person.age)
                                                            #    hasattr()
# class Person:
#     name='john'
#     age=35
#     country='India'
# x=hasattr(Person,'age')
# print(x)

#                                                                setattr()

# class Person:
#     name='john'
#     age=35
#     country='India'
# # # # x=getattr(Person,'age')
# # # # print(x)
# # # x=getattr(Person,'age1','none')
# # # print(x)
# # setattr(Person,'age',40)
# setattr(Person,'age1',40)
# # x=getattr(Person,'age')
# # print(x)
# x=getattr(Person,'age1','none')
# print(x)

# #                                                                issubclass()

# create a clas student with clas varaible school
# a)create a parametrized constructr wth id nme and age
# b)create instance of the class with id=1 name=sara age=10 and id=2 name=jose age=20
# c)acces values of attribute of an instnce using buildin fn 
# d)chnge the nme attribite frm jose to chris of defined instance
# e)check if class student has place attribute if class student has no plce attribute then create it using the buildin method

# wrute a python progrm to calculate A dog 's' age in dog's year note:for the frst 2 year a dog yr=10.5 human yrs after tht each dog year equals 4 human years



# a=int(input('enter human age'))
# if a<=2:
#     print(a*10.5)
# else:
#     print((a-2)*4+21)

# class Student:
#     school='arafa'
#     def __init__(self,i,n,a):
#         self.id=i
#         self.name=n
#         self.age=a
# studen1=Student(1,'sara',10)
# # student2=Student(2,'jose',20)
# x=getattr(studen1,'id')
# print(x)
# x=getattr(studen1,'name')
# print(x)
# x=getattr(studen1,'age')
# print(x)
# setattr(studen1,'name','chris')
# x=getattr(studen1,'name')
# print(x)
# x=hasattr(studen1,'place')
# print(x)
# if x==False:
#     setattr(studen1,'place','ernklm')
# # setattr(studen1,'place','ernklm')
# print(studen1.place)
# x=getattr(studen1,'place')
# print(x)


        
# wrte a python clss named student with 2 attribute studnt name , mark
#  modify the attrbute values of the said class and bring the original and modified values of the said attribute


# class Student:
#     name='anu'
#     mark=200
# stud1=Student()
# x=getattr(stud1,'name')
# print(x)
# y=getattr(stud1,'mark')
# print(y)
# setattr(stud1,'name','anuthomas')
# setattr(stud1,'mark','100')
# x=getattr(stud1,'name')
# print(x)
# y=getattr(stud1,'mark')
# print(y)
 
# a=350
# if a>200:
#     print(100*5+(a-200)*10)
# elif a>100:
#     print((a-100)*5)
# else:
#     print('no charge')


# create a python class named bank_account with attribute for the account holder's name and balance
# implement methods for deposit and withdrawal ensuring that the balance cannot go below Zero
#     create an obj and demonstrate deposit and withdrawal operations


# class Bank_Account:
#     def __init__(self,n,b):
#         self.name=n
#         self.balance=b
#     def deposit(self):
#         x=int(input('enter ammount to deposit'))
#         self.balance=self.balance+x
#         print(self.balance)
#     def withdrawal(self):
#         y=int(input('enter ammount to withdraw'))
#         if self.balance>y:
#             print(self.balance-y,'new balance')
#         else:
#             print('not enough balance')
    
# accnt1=Bank_Account('anu',100)
# accnt1.deposit()
# accnt1.withdrawal()


# define a base class shape with methods to calculate area and perimeter
# create subclasses for specific shapes like circle and rectangle
#     implement these methods in the subclasses and calclte the area and the perimeter for a circle and a rectangle

