#padding
a='hello'
print(a.zfill(55))


var='******hi*****'
print(var.rjust(10))
print(var.rjust(14 ,'2'))
print(var.ljust(100,'4'))
# print(var.ljust(10,'*'))
print(var.center(20,'%'))
# # print(var.zfill(10))
var='*******a****This is a * * good example***a***'
var='8900000'
print(var.lstrip('8'))
# print(var.rstrip('*'))
# print(var.strip('*'))
# print(var.strip('*'))
# a='hiiiiii777\n'
# print(a.rstrip())
var='welcome'
# print(var)
# print(var.find('p'))
# print(var.find('e',2,9))
# print(var.find('e',8,-1))
# print(var.find('i',2,5))
# print(var.rfind('e',3,9))
# # print(var.index('e'))
# # print(var.index('j'))


# a='well******'
# print(a.rjust(15,'2'))
# # print(a.ljust(13,'7'))
# print(a.center(22,'5'))
# print(a.zfill(10))


# a='fathima'
# # print(a.find('a',3,8))
# # print(a.rfind('a',2,5))
# print(a.index('a',2,5))


7 

a='ghjkt'
b='vhjivw'
b=b[::-1]
c=''
l=min(len(a),len(b))

for i in range(l):
    c+=a[i]+b[i]
    print(c)
c+=a[l:]+b[l:]
print(c)
