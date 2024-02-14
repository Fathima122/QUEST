# import unittest
# from c import *

# class Multiply_Testcase(unittest.TestCase):
#     def test_multi_1(self):
#         self.assertEqual(multiply(4,2),34)
#     def test_multiph3(self):
#         self.assertEqual(multiply('3','5'),15)
     


# unittest.main()


#                                      exception handling


# the try block lets you test a block of code for errors
# the except block lets you handle the error
# the finally block lets you execute code,regardless of the result of the try- and except blocks

# x='hai'
# print(x)

# try:
#     # x=9
#     print(x)
# except:
#     print('error occurred')

# try:
#     v=5
#     print(v)
# except:
#     print('something went wrong')
# else:
#     print('Nothing went wrong')
# finally:
#     print('cmplt')

# try:
#     y='hai'
#     a=[3,65,4,2]
#     print(a[1])
#     print(y)
# except NameError:
#     print('name error went wrong')
# except IndexError:
#     print('indendation')
# finally:
#     print('the try except is finished')


# x=-21
# if x<0:
#     raise Exception('sorry ,no numbers below zero')

# x='6'
# if not type(x) is int:
    # raise IndexError('Only integers are dfsfdfdfdfdfds')

# a=4/0
# print(a)

# class Lessthan10(Exception):
#     def __self__(self):
#         return 'Enter Number greater than 10'
# try:
#     a=5/10

#     a=int(input('enter the number greater than 10: '))
#     if a<10:
#         raise Lessthan10()
#     b=int(input('enter the number:'))

# except ZeroDivisionError as d:
#     print(d)
#     print(ZeroDivisionError)
# #     print('enter a non')

