# x=lambda a:10+8
# print(x)
# print(x(2))
# x=lambda a:10+a
# print(x(2))

# an anonymous inlne fn consist of a singl expre which is evaluatd whn fn is clld.
# syntx:lambda[parameters]:expresiion



# x2=lambda a,b,c: print(c)
# x2(3,2,1)
# print(x2(3,2,1))

# x=lambda a: v=2*a
# print(x(2))

# x1=lambda a:10+a
# print(x1(9))

# def myfun(n):
#     return lambda a:a*n                             #lambda a:a*2


# z=myfun(5)
# print(z(3))


# BUILT IN METHOD OF LAMBDA
# filter()
# MAP()#BUILT IN METHOD OF LAMBDA
# REDUCE()


# li=[5,7,22,97,54,62,77,23,73,61]
# final_list=list(filter(lambda x:(x%2 !=0) ,li))
# print(final_list)


# li=[5,7,22,97,54,62,77,23,73,61]
# final_list=list(map(lambda x:x*2,li))
# print(final_list)


# from functools import reduce
# li=[5,7,22,97,54,62,77,23,73,61]
# sum=reduce((lambda x,y:x-y),li)
# print(sum)

# hw are lmbda fn useful
# fn=lambda x: return x
# print(fn(2))   lambda cannot contain return 
# wht are thw common fnctnal progrmng methods  --->filtr map reduce

# z=(lambda x:(x+3)*5/2)(3)
# print(z)



# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# x=lambda a:10+3
# # print(x)
# # print(x(1))
# print(x(2))

# x=lambda a:2*a
# print(x(2))

# x=lambda a,b,c:a+a
# print(x(1,2,3))

# def myfun(n):
#    return lambda a:a+n



# z=myfun(5)
# print(z(3))