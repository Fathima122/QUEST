# class myAge:
#     age=36
# class myObj(myAge):
#     name='john'
#     age=8
# x=issubclass(myObj,myAge)
# x=issubclass(myAge,myObj)
# print(x)

# super()

# class Parent:
#     def __init__(self,txt):
#         self.message=txt
#         print('................')
#     def printmessage(self):
#         print(self.message)
# class Child(Parent):
#     def __init__(self,txt):
#         print('child aaaaaaaaaaaa')
#         # Parent.__init__(self,txt)
#         super().__init__(txt)
#     def printmessage(self):
#         print('python')
#     def show(self):
#         print('welcome')
#         Parent.printmessage(self)
# class Child1(Parent,Child):
#     def __init__(self,txt):
#         super().__init__(txt)
#     def  show(self):
#         print('welcome')
#         super().printmessage()
# anu=Child1('happy')
# anu.show()

# ammu=Child('piiiiii')
# ammu.printmessage()
# ammu.show()
# class Student:
#     def __init__(self):
#         print('iam student')
#     def mark(self):
#         print('obtain mark')
#     def study(self):
#         print('study for mark')
# class Dancer(Student):
#     def __init__(self,a):
#         self.msg=a
#         super().__init__()
#         print('iam dancer')
#         print (self.msg)
#     def study(self):
#         super().study()
#         # Student.study(self)
#         print('study for passion')
# anu=Dancer('hii')
# anu.study()
    


# from abc import ABC,abstractmethod

# class Polygon(ABC):
#     @abstractmethod   #decor
#     def area(self):
#         pass
#     def mymthd(self):
#         print('hello')
# class Rectangle(Polygon):
#     def hii(self):
#         print('iam rectangle')
#     def area(self):
#         print('rect area')

#     def area1(self):
#         print('rect area')

# book= Rectangle()
# book.area()
# a=Polygon()  
#  object creation 