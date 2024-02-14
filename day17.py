# EXTEND
# lst4=[1,3,'hai']
# lst4.append('hajk')
# lst4.extend('fhjdk')
# print(lst4)


### remove elements


# vowels=['a','e','i','o','u','a']
# vowels.remove('a')
# print(vowels)

# vowels=['a','e','i','o','u','e']
# # # # print(vowels)
# del vowels[1:4:2]
# print(vowels)

# constants=['b','c','d','g']
# # constants.pop()
# constants.pop(2)
# print(constants)

# s=['n','g',2,3,4,5,6,67,7]
# s.clear()
# print(s)

# r=[2,3,4]
# r[0:2]=32,1
# print(r)


a=[1,2,3,4,2,'hai']
# b=[31,5,5,6,'jj']
# # print(a+b)
# a.append(b)
# # a.extend(b)
# # # print(a)
# print(a.index(3,1,9))
# print(a.index(2,3,9))

# del a[2]
# a.remove(1)
# print(a)

# a.pop(5)
# print(a)
# a=[]
# a.clear()
# print(a)

#homework
#search element 


# a=[]
# size=int(input('enter size of list:'))
# for i in range(size):
#     val=(input('enter elements'))
#     a.append(val)           #input
# key=(input('enter element to search'))
# flag=0      #setting flag to search
# for i in range(size):
#     if a[i]==key:
#         flag=1
#         postn=i+1
#         break
# if flag==1:
#     print('element found at',postn,'position')
# else:
#     print('not element found')

# array are sme


# a=[]
# size=int(input('enter size of list:'))
# for i in range(size):
#     val=(input('enter elements'))
#     a.append(val)

# b=[]
# size1=int(input('enter size of list:'))
# for i in range(size1):
#     val1=(input('enter elements'))
#     b.append(val1)
# if size!=size1:
#     print('the arrays are different')
# else:
#     for i in range(size):
#         if a[i]!=b[i]:
#             print('the arrays are different')
#             break
#     else:
#         print('the arrays are same')

#ascending order/descending order

# a=[6,5,4,3,8,1]

# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
# print(a)


# l1=['zero','one','two','three','four','five','six','seven','eight','nine' ]
# l2=['ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','eighteen','nineteen']
# l3=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
# n=int(input('enter no'))
# if n<=9:
#     print(l1[n])
# elif n<20 and n>=10:
#     print(l2[n-10])
# elif n>=20 and n<100:
#     o=n%10
#     t=n//10
