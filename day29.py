# def add(a,b):
#     print('sum is',a+b)
# def sub(a,b):
#     print 


# def add(*a):
#     # print(a+b)
#     print(a)
# # add(4,5,7,7)
# add([4,5,7,7])


# no_items=int(input('enter items:'))
# p=[]
# for i in range(no_items):
#     pro=int(input('amount:'))
#     p.append(pro)
# print(p)

# def total(*a):
#     sum=0
#     for i in a:
#         for j in i:
#             sum+=j
#     print(sum)
# total(p)

# def details(**place):
#     print(place)
# details(name='anu',place='eklm',phno=7678,email='anu@gmail.com')

# return

# def sum(s1,s2,s3):
#     s=s1+s2+s3
#     # return s
#     print(s)
# def avg(s,n):
#     s=s1+s2+s3
#     a=s/n
#     print('avg',a)
# b=sum(2,3,4)
# print(b)
# avg(b,3)
#                                                                       homework

# define a fn tht accepts lower case wrds and returns uppercase wrds
# define a fn tht accepts radius and return the area of a circle
# define a fn tht returns factorial of a no
# define a fn which counts vowels and constants in a wrd
# # define a fn tht accepts a no and return wether a no is even or odd
# write a fn ,fizzbuzz,withn a single integer arg named value.if the value is evenly divisible by 3,reurn the string 'fizz'.if the value is evenly div by 5,return the str 'buzz'.if the value is evenly div by both 3 and 5,retn 'fizzbuzz'.finally ,if none of these apply,retrn an empty string
 
# def lower():
#     a=input('enter string')
#     print(a.lower())
#     u=print(a.upper())
# lower()


# def lower(a):
#     print(a.upper())
# b=input('enter a string')
# lower(b)


# def radius(y):
#     area=3.14*(r*r)
#     print(area)
# r=int(input('enter radius '))
# radius(r)

# def fac(a):
#     fact=1
#     for i in range(1,a+1):
#         fact*=i
#     print(fact)
# c=int(input('enter no'))
# fac(c)


# def oddeven(a):
#     if a%2==0:
#         print('even no')
#     else:
#         print('odd no')
# x=int(input('enter no. to check'))
# oddeven(x)



# def vowelconst(a):
#     countv=0
#     countc=0
#     s='aeiouAEIOU'
#     for i in a:
#         if i.isnumeric():
#             countc+=1
#         elif i in s:
#             countv+=1
#     print(countc)
#     print(countv)
# c=input('enter string')
# vowelconst(c)


# def fizzbuzz(input):
#     if value%3==0 and value%5==0:
#         return 'fizzbuzz'
#     elif value%3==0:
#         return 'fizz'
#     elif value%5==0:
#         return 'buzz'
#     else:
#         return ''
# value=int(input('enter a value'))
# f=fizzbuzz(value)
# print(f)