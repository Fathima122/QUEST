# def febinocci(a):
#     b=0
#     c=1
#     i=0
#     while a>i:
#         print(b)
#         d=b+c
#         b=c
#         c=d
#         i+=1
# a=int(input('enter no'))  
# febinocci(a)


# wrte a recursive fn tht accepts a no as its arg and return the sum of didgits

# def sumDigits(n):
#     if (n<10):
#         return n
#     else:
#         return n%10 + sumDigits(n//10)
    
# number=23456
# print('sum of digits ',number ,'is', sumDigits(number))



# wrte a recursive fn tht  calculate sum of frst 10 natural no.s



# 1-register 2-login 3-exit

user_data={}

def register():
    username=input('enter a username:')
    password=input('enter a password')
    user_data[username]=password
    print('registration successful!')

def login():
    username=input('enter a username:')
    password=input('enter a password')
    if username in user_data and user_data[username]==password:
        print('login successful!')
    else:
        print('login failed.please check your username and password')
while True:
    print('\nMain menu:')
    print('1.registe')
    print('2. login')
    print('3.exit')

    choice=input('enter your choice')
    if choice=='1':
        register()
    elif choice=='2':
        login()
    elif choice=='3':
        print('goodbye!')
        break
    else:
        print('invalid choice')
