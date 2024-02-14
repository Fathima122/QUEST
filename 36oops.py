# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#        return ( self.length*self.width)
#     def perimeter(self):
#        return ( 2*(self.length+self.width))
#     def  display(self):
#         print(self.length,'-length')
#         print(self.width,'-widtth')
#         print(self.area())
#         print(self.perimeter())

# rec1=Rectangle(4,6)
# rec1.display() 
# class Parallelopipe(Rectangle):
#     def __init__(self,length,width,c):
#         self.height=c
#         Rectangle.__init__(self,length,width)

#     def volume(self):
#         print(self.length*self.width*self.height)

# par=Parallelopipe(10,20,30)
# par.display()
# par.volume( )
# create a pythn clss prson with attributes nma and age of type string
#    crete a disply methd tht displays the nme and age of an obj created via a person clss
#      create a chld class student which inherits frm the persn clss  which also has a section attribute
#       crete a mthd disply student tht displys tge nme age and sectn of an obj creted via the student class

# class Person:
#     def __init__(self,n,a):

#         self.name=n
#         self.age=a
#     def display(self):
#         print(self.name)
#         print(self.age)

# person1=Person('anu','89')
# person1.display()
# class Student(Person):
#     def __init__(self,n,a,s):
#         self.section=s
#         Person.__init__(self,n,a)
#     def display(self):
#         Person.display(self)
#         print(self.section,'-section')


# ammu=Student('ammoos',34,'section')
# ammu.display()
        









