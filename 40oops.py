# class Calculator:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):    #method overloading doesnt wrk on python
#         print(a+b-c)
# c1=Calculator()
# c1.add(2,3)
# eg, a=6
# a='jai'
# print(a)

# create a abstrct class wuth the basic fnclites of a clac annf then implemnt the clss with proper fnctnlts
# tghe abstrc should have all mthds like add sub mul and div wuth basic implemention

# from abc import ABC,abstractmethod

# class Calculator(ABC):
#     @abstractmethod
#     def add(self):
#         pass
#     @abstractmethod
#     def sub(self):
#         pass
#     @abstractmethod
#     def mul(self):
#         pass
#     @abstractmethod
#     def div(self):
#         pass
# class Normal_Calculator(Calculator):
#     def __init__(self,a,b):
#         self.number1=a
#         self.number2=b
#     def add(self):
#         print(self.number1+self.number2)
#     def sub(self):
#         print(self.number1-self.number2)
#     def mul(self):
#         print(self.number1*self.number2)
#     def div(self):
#         print(self.number1/self.number2)
# cal1=Normal_Calculator(10,8)
# cal1.add()
# cal1.sub()
# cal1.mul()
# cal1.div()


# public

# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print('age',self.age,'name',self.name)
# a=A('anu',12)
# a.display()

# protected

# class A:

#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def _display(self):
#         print('age',self._age,'name',self._name)
# a=A('anu',12)
# a._display()

# class B(A):
#     def __init__(self,name,age):
#         A.__init__(self,name,age)
#     def displaydetails(self):
#         self._display()
# b=B('ammu',55)
# b.displaydetails()

# ---------------------access specifiers in python==================
# 1.public 
# 2.protected
# 3.private


#                                                         1.public 

# class Student:
#     def __init__(self,name,):
#         self.name=name
#     def display(self):
# #         print('hii myself',self.name,'from student class' )
# # s1=Student('anu')
# # print(s1.name)
# # s1.display()

# #                                                              2.protected

# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self._rollno=rollno
#     def display(self):
#         print('hii myself',self.name,' with roll no ',self._rollno,'from student class' )
# class Branch(Student):
#     pass
# # b1=Branch('nela',22)
# # print(b1.name)
# # print(b1._rollno)
# s1=Student('anu',55)
# print(s1.name)
# s1.name='anna'
# s1._rollno=45
# s1.display()

#                                                                    3.private

# class Student:
#     def __init__(self,name,rollno,age):
#         self.name=name
#         self._rollno=rollno
#         self.__age=age
#     def display(self):
#         print('hii myself',self.name,' with roll no ',self._rollno,'from student class',self.__age )

# s1=Student('rahul',22,18)
# print(s1.__age)
# s1.display()
