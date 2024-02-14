#given an lst of elemnts,remove the duplicate element
# a=[2,4,56,67,2,4,56] 
# c=set(a)
# print(c)


#read a string and find the no. of unique characts in it
# a=input('enter a string')
# c=set(a)
# print(c)
# d=list(a)
# print(d)
# for i in c: 
#     d.remove(i)
# e=set(d)
# o=len(c)-len(e)
# print(o)


# gvn 2 set of no.s wrte a pythn prgrm to find the missing nos. in the 2nd set as compared to the 1st
# a={1,2,3,4,5}
# b={1,3,5,7,9}
# missing_no=[]
# for i in a:
#     if i not in b:
#         missing_no.append(i)
# print(missing_no)
# m=set(missing_no)
# print(m)

#membeship operations

# a={1,2,3,9}
# print(1 in a)
# print(6 not in a)



a={1,2,3,4,5}
b={4,5,6,7,8}
print('union=',a|b)
print('intersection=',a&b)
print('difference=',a-b)
print('symmetric difference=',a^b)

nos={1,2,3,4,5,6,7,8,9,10}
even={2,4,6,8,10} 
odd={1,3,5,7,9}
print(even.isdisjoint(odd))
print(odd.issuperset(nos))
print(odd.issubset(nos)) 


# def add():
#     print(3+4)

# add()
# add()

# def add(a,b):
#     print(a)
#     print(b)      positional argument
#     print(a+b)
# add(2,3)
# add(4,8)

# def details(n,p):
#     print('my name is ',n ,'my place is ',p)
# details(p='anu',n='ernklm')
# details(n='anuuu',p='ernklmla')   keyword argument


# def add(a,b=6):
#     print(a)
#     print(b)
#     print(a+b)
# add(3,9)
 