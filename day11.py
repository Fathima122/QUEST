# a='hel223lo'
# sum=0
# for i in a:
#     if i.isnumeric()==True:
#         sum=sum+int(i)
# print(sum)

# a='hjkjhfjdaii'
# countv=0
# for i in a:
#     if i in 'aeiouAEIOU':
#         countv+=1
#     else:
#         print('not vowel')
# print(countv)

# a='restart'
# print(a.replace('r','h'))

a=(input('enter a string'))
b=len(a)
c=a.replace('ing','ly')
if 'ing' in a: 
    print(c)
elif b>=3:
    a+='ing'
    print(a)
else:
    print(a)

# a=input('enter a string')
# b=len(a)
# lastoccurrence=a.rfind('ing')
# if lastoccurrence>=0:
#     output=a[:lastoccurrence]+'ly'
#     print(output)
# elif b>=3:
#     a+='ing'
#     print(a)
# else:
#     print(a)


# a='have a nice day'
# b=(a.split())
# print(b)
# for i in  b:
#     if len(i)%2==0:
#         print(i)
#     # else:
    #     print(b)

# a='dhjkld'
# print(a.rfind('d'))


    

      



