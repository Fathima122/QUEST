#  wrte a python clss named student with 2 attribute studnt name , mark
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
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#     def area(self):
#         print (self.length*self.width)
#     def perimeter(self):
#         print (2*(self.length+self.width))
# # rec1=Rectangle(10,20)
# # print(rec1.area())
# class Circle(Shape):
#     def __init__(self,r):
#         self.radius=r
    
#     def area(self):
#         print (3.14*(self.radius**2))
#     def perimeter(self):
#         print (2*3.14*self.radius)
# rec1=Rectangle(2,4)
# rec1.area()
# rec1.perimeter()
# s=Shape() doesnt wrk

