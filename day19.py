# g=[2,3,1,3,6,'hai']    #error due to string
# print(sum(g))                                 

# g=['dd','ff']
# v=''
# for i in g:
#     v+=i
#     print(v)


# g=[2,3,435,5,6,4] 
# g.sort()   #error
# #  sort assigning is not possible
# print(g)   

# lsta=['fg',0,1,2,3,45,6]
# lsta.reverse()
# print(lsta)

# g=[1,4,8,2,4]
# g.sort(reverse=True)
# print(g)

# lstb=[1,'a','gh']
# i=iter(lstb)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))  
# print(next(i))



# a='get'
# b='set'
# m=[i+j   for i in a for j in b]
# print(m)

# a=[i for i in range(5)]
# print(a)

# n=[2,43,67,52,77,12]
# a=[]
# for i in n:
#     if i%2==0:
#         a.append(i)
# print(a) 

# a=[i for i in n if i%2==0]
# print(a)


# a=['e' if i%2==0  else 'o'  for i in n]
# print(a)


a=[1,2,3,4,9,0]
# print(sum(a))
# print(a.sort())
# a.sort(reverse=True)
# print(a)
# # a.sort(reverse=True)
# # a.reverse()
# # print(a)
# i=iter(a)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# ab=[i for i in a if i%2==0]
# ab=['e' if  i%2==0  else 'o' for i in a ]
# print(ab)

#homework
# index wise adding elements


# lst1=['m','na','i','ke']
# lst2=['y','me','s','lly'] 

# re=[]
# for i in range(4):
#     re.append(lst1[i]+lst2[i])
# print(re)

# a=[lst1[i]+lst2[i] for i in range(4)]
# print(a)




# list1=['hello','take']
# list2=['dear','sir']
# if len(list1)<len(list2):
#     size=len(list)
# else:
#     size=len(list2)
# r=[]
# for i in range(size):
#     r.append(list1[i]+list2[i])
# print(r) 


# r=[]
# if len(list1)==len(list2):
#     for i in range(len(list1)):
#         r.append(list1[i]+list2[i])
# print(r)

# r=[list1[i]+list2[i] for i in range(len(list2)) if len(list1)==len(list2)]
# print(r)
# a=[int(input('enter no')) for i in range(5)]
# print(a)
# for i in range(5):
#     a.append(int(input('enter no')))
# print(a)
# n=[1,2,3]
# a=[i*2 for i in n]
# print(a)



l1=['m','na','i','ke']
l2=['y','me','s','lly','sghjakjsk'] 
# newlist=[]

l=min(len(l1),len(l2))
# for i in range(l):
#     newlist.append(l1[i]+l2[i])
# newlist.extend(l1[l:]+l2[l:])
# print(newlist)

 