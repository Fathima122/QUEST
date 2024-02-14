#1,
# a=input('enter a string')
# # print(len(a))
# count=0
# for i in range(len(a)):
#     count+=1
# print('length of string is :',count)

# 2,
# s='google.com'
# d={}
# for i in s:
#     d[i]=0
# for i in s:
#     d[i]=d[i]+1
# print(d)
                                                                               #or     
# for i in s:
#     if i in d:
#         n=d[i]
#         d[i]=n+1

    
#     else:
#         d[i]=1
# print(d)

#3,

# sample='w3resource'
# new=''
# if len(sample)<2:
#     print('return empty string')
# else:
#     new=sample[:2]+sample[-2:]
# print(new)
#4,


# sample='restart'
# print(sample.rfind('r',2,9))
# sample=sample.replace('r','$')
# print(sample)

# ch=sample[0]
# modifiedstr=sample[0]+sample[1:].replace('r','$')
# print(modifiedstr)

#5,                  python prgm to get a singl string frm 2 gvn strn seperated by a spzce and swap frst 2 chr of each strn

# sample='abc'
# sample1='xyz'
# # op='xyc abz'
# newsample=sample1[:2]+sample[2:]
# newsample1=sample[:2]+sample1[2:]
# new=newsample+' '+newsample1
# print(new)

#                                                                 list(1,2,3,4,5)

# a=[]
# size=int(input('enter size of list:'))
# sum=0
# for i in range(size):
#     val=int(input('enter elements'))
#     a.append(val)
#     sum=sum+val
# print(sum)

# a=[1,4,5,10,7,8]
# mul=1
# for i in a:
#     mul=mul*i
# print(mul)

# lar1,6gerst no. frm lst,smallest
# a=[2,7,9,76,9790,0]
# a=[]
# size=int(input('enter size of list:'))
# for i in range(size):
#     val=int(input('enter elements'))
#     a.append(val)
# max=a[0]
# for i in a:
#     if i>a[0]:
#         max=i
# print(max)

# min=a[0]
# for i in a:
#     if i<min:
#         min=i
# print(min)


# pgrm to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# SampleList = ['abc', 'xyz', 'aba', '1221']
# count=0
# for i in SampleList:
#     if len(i)>=2 and i[0]==i[-1]:
#         count+=1
# print(count)

# # 6, 
# sample=input('enter a string')
# if len(sample)<3:
#     print(sample)
# elif sample[-3:]=='ing':
#     print(sample+'ly')
# else:
#     print(sample+'ing')


#7 
# a='the lyrics is not that poor'
# pos=a.find('not')
# pos1=a.find('poor')
# print(pos)
# print(pos1)
# if pos<pos1:
#     print(a[:pos]+'good')
# else:
#     print(a)

#8
# a=['apple','grapes','pineapple','pomegranite','carrots']
# logest_word=''
# logest_length=0
# for i in a:
#     if len(i)>logest_length:
#         logest_word=i
#         logest_length=len(i)
# print('longest word is',logest_word)
# print('longest length is',logest_length)

# #9
# a=input('enter a non empty string')
# n=int(input('enter the index of the character to remove'))
# if n<0 or n>=len(a):
#     print('invalid index')
# else:
#     new=a[:n]+a[n+1:]
#     print(new)


# a=input('enter a string')
# new=a[-1]+a[1:-1]+a[0]
# print(new)

# a=input('enter string')

# # print(a[0::2])

# w={}
# c=a.split()
# for i in c:
#     if i in w:
#         n=w[i]
#         w[i]=n+1
#     else:
#         w[i]=1
# print(w)

# that takes input from the user and displays that input back in upper and lower cases.

# a=input('enter a string')
# print(a.upper())
# print(a.lower())

# that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form 

# a=input('comma-separated sequence of words')
# C=a.split(',')
# C.sort()
# print(C)

# Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# def strng(a):
#     if len(a)<3:
#         return a
#     else:
#         return (a[:3])
    
# z=strng(input('enter a string'))
# print(z)


# Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# a='https://www.w3resource.com/python-exercises'
# new=a.rsplit('/',1)
# print(new)
# print(a.split('-')[0])


# def insert_strng(original_string,n_string):
#     middle_index=len(original_string)//2
#     new_string=original_string[:middle_index]+n_string+original_string[middle_index:]
#     return new_string
# z=insert_strng('helloui, world','beauty')
# print(z)



# def copy(a):
#     if len(a)>2:
#         new=4*a[len(a)-2:]
#         print(new)
# copy('python')

# def reverse(a):
#     if len(a)%2==0:
#         return (a[::-1])
#     else:
#         return a



# z=reverse('car')
# print(z)
#                                   # or

# def reverse(a):
#     if len(a)%2==0:
#         s=''
#         for i in a:
#             s=i+s
#         return s
    
# b=input('enter a string')
# z=reverse(b)
# print(z)


# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

# def upper(a):
#     uppercount=0
#     for i in a[0:4]:
#         if i==i.upper():
#             uppercount+=1
#     if uppercount>=2:
#         print(a.upper())


# upper('wElcOMe')

# # Write a Python program to sort a string lexicographically.
# a=input('enter a string')
# s=''.join((sorted(a)))
# print(s)



# Write a Python program to remove a newline in Python.
# str1='Python Exercises\n'
# print(str1)
# print(str1.rstrip())


# # Write a Python program to check whether a string starts with specified characters.
# a='w3resuorce'
# print(a.startswith('w3r'))

 

# Write a Python program to display formatted text (width=50) as output.


# Write a Python program to remove existing indentation from all of the lines in a given text.  

# Write a Python program to print the following numbers up to 2 decimal places.
# n=12345
# print('the decimal o is {n:.2f}'.format(n=789))


# Write a Python program to print the following numbers up to 2 decimal places with a sign.
# print('the no. with decimal place is {n:+.2f}'.format(n=3.14567))


# Write a Python program to print the following positive and negative numbers with no decimal places.
# print('the no. with no decimal places is {a:.0f}'.format(a=3567.78))

# Write a Python program to print the following integers with zeros to the left of the specified width.
# a='3456'
# a='123.900'
# a='-5890'
# a='123'
# print(a.zfill(6))

# Write a Python program to print the following integers with '*' to the right of the specified width.
# a='1234'
# print(a.rjust(17,'*'))


  # Write a Python program to display a number with a comma separator.
# print('the no. with comma seperator is {a:,}'.format(a=23455900))

# # Write a Python program to format a number with a percentage.
# print('the no. with a percentage is {a:.2%}'.format(a=0.25))

# Write a Python program to display a number in left, right, and center aligned with a width of 10.
# a='69'
# print(a.ljust(10,))
# print(a.rjust(10))
# print(a.center(10))


#  Write a Python program to count occurrences of a substring in a string.
# a='the animal run from jungle and the forest liesd'
# print(a.count('animal'))
# print(a.count('jungle'))
# print(a.count('the'))


# Write a Python program to reverse a string.
# a=input('enter a string')
# s=''
# for i in a:
#     s=i+s
# print(s)
# a='6789vcbjkl566'
# print(a[::-1])

# # . Write a Python program to reverse words in a string
# a='animal has four eyes we have won'
# b=a.split()
# # print(b)
# c=''
# for i in b:
#     c=' '+i+c
# # print(c)
# print(c.lstrip(' '))

# Write a Python program to strip a set of characters from a string.
# a='    hello,World!       '
# c='    ,!     '
# for i in c:
    
#   a=a.replace(i,'')
# print(a)

# a=input('enter a string')
# c='aeiou'
# for i in c:
#   a=a.replace(i,'')
# print(a)


# Write a Python program to count repeated characters in a string.
# a=input('enter a string')
# w={}
# # print(a.count('l'))
# for i in a:
#     if i in w:
#         n=w[i]
#         w[i]=n+1
#     else:
#         w[i]=1
# for i in w:
#     if w[i]>1:
#         print(w[i],i)

# Sample string: 'thequickbrownfoxjumpsoverthelazydog'




# Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.


# not taught






# Write a Python program to print the index of a character in a string.
# a='hello'
# print(a.index('h',0,8))
# print(a.index('e'))

# Write a Python program to check whether a string contains all letters of the alphabet.
# alphabet=set('abcdefghijklmnopqrstuvwxyz')
# a=input('enter a string')
# for i in a.lower():
#     if i in alphabet:
#         alphabet.remove(i)
# print(len(alphabet)==0)    


    


# Write a Python program to convert a given string into a list of words.
# a='the quick brown fox'
# b=a.split()
# print(b)


# Write a Python program to lowercase the first n characters in a string.
# a=input('enter a string')
# print(a[:3].lower()+a[3:])


# 48. Write a Python program to swap commas and dots in a string.
# a= '32.054,23'
# # c='.,'
# # Expected Output: "32,054.23"
# a=a.replace('.','third')
# a=a.replace(',','.')
# a=a.replace('third',',')
# print(a)

#Write a Python program to count and display vowels in text.

# a=input('enter a string')
# countv=0
# for i in a:
#     if i in 'aeiouAEIOU':
#         countv+=1
#         print(i)
# print('total count=',countv)





# 50. Write a Python program to split a string on the last occurrence of the delimiter.
# a='w,3,r,e,s,o,u,r,c,e'
# print(a.rsplit(',',1))
# print(a.rsplit(',',2))





# 51. Write a Python program to find the first non-repeating character in a given string.

# a=input('enter a string')
# c={}
# for i in a:
#     if i in c:
#          n=c[i]
#          c[i]=n+1
#     else:
#       c[i]=1
# for i in c:
#     if c[i]==1:
#         print(i)
#         break
# else:
#     print('there is  no non repeating character')



















#cc Write a Python program to print all permutations with a given repetition number of characters of a given string.
# Click me to see the sample solution
#



# # 53. Write a Python program to find the first repeated character in a given string.
# a=input('enter a string')
# c={}
# for i in a:
#     if i in c:
#         n=c[i]
#         c[i]=n+1
#     else:
#       c[i]=1
# for i in c:
#    if c[i]==2:
#       print(i,index(i))
#       break
# else:
#   print('None')


# 54. Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.
# a=input('enter a string')
# c={}
# for i in a:
#     if i in c:
#         n=c[i]
#         c[i]=n+1
#     else:
#        c[i]=1 
# for i in c:
#     if c[i]==2:
#         print(i,a.index(i))
#         break
# else:
#     print('none')






# 55.Write a Python program to find the first repeated word in a given string.
# a=input('enter a string')
# b=a.split()
# c={}
# for i in b:
#     if i in c:
#         n=c[i]
#         c[i]=n+1
#     else:
#         c[i]=1
# for i in c:
#     if c[i]==2:
#         print(i)
#         break
# else:
#     print('there is no repeated wd')
    










# 56. Write a Python program to find the second most repeated word in a given string. 


# a=input('enter a string')
# b=a.split()
# c={}
# for i in b:
#     if i in c:
#         n=c[i]
#         c[i]=n+1
#     else:
#         c[i]=1
# d=sorted(c,key=c.get)
# print(d[-2])


# Write a Python program to remove spaces from a given string.
# a=input('enter a string')
# print(a.replace(' ',''))


# 58. Write a Python program to move spaces to the front of a given string.
# a=input('enter a string')
# spaces=''
# for i in a:
#     if i==' ':
#         spaces+=i
# print(spaces+a.replace(' ',''))
        

#  59. Write a Python program to find the maximum number of characters in a given string.
# a=input('enter a string')
# max_count=0
# max_char=''
# for i in a:
#     count=0
#     for j in a:
#         if i==j:
#             count+=1
#     if count>max_count:
#         max_char=i
# print('maximum number of characters : ',max_char)

# Write a Python program to capitalize the first and last letters of each word in a given string.
# a=input('enter a string')
# b=a.split()
# string=''
# for i in b:
#     new=i[0].upper()+i[1:-1]+i[-1].upper()+' '
#     string+=new
# print(string)



# 61. Write a Python program to remove duplicate characters from a given string.


# a=input('enter a string')
# d=''
# for i in a:
#     if i not in d:
#         d=d+i
# print(d)

# 62. Write a Python program to compute the sum of the digits in a given string.
# a=input('enter a string')
# sum=0
# for i in a:
#     if i.isdigit()==True:
#         z=int(i)
# #         sum+=z
# print(sum)


#  Write a Python program to remove leading zeros from an IP address

# a=input('enter a string')
# print(a.lstrip('0'))
# not taught



# Write a Python program to find the maximum length of consecutive 0's in a given binary string
# a='100010100001111'
# count=0
# max_len=0
# for i in a:
#     if i=='0':
#         count+=1
#         # print(count)
#         max_len=max(count,max_len)
#     else:
#         count=0
# # print(max_len)

# Write a Python program to find all the common characters in lexicographical order from two given lower case strings. 
# If there are no similar letters print "No common characters".



# a='w3resource'
# b='python and swift'
# c=[]
# for i in a:
#     if i   in b:
#         c.append(i)
    
# if len(c)==0:
#     print('no common characters')
# else:
#     c.sort()
#     print(c)

#     result=''
#     for i in c:
#         result+=i
#     print(result)


# Write a Python program to make two given strings (lower case, may or may not be of the same length)
# anagrams without removing any characters from any of the strings.
# a=input('enter a string')
# b=input('enter a string')

# l=list(a)
# l1=list(b)

# l.sort()
# l1.sort()

# if l==l1:
#     print("The two strings are anagrams.")
# else:
#     print("The two strings are not anagrams.")



# 67. Write a Python program to remove all consecutive duplicates of a given string.

# a=input('enter  a string')
# d=''
# for i in a:
#     if i not in d:
#         d+=i
# print(d)




# Write a Python program to generate two strings from a given string. 
# For the first string, use the characters that occur only once, 
# and for the second, use the characters that occur multiple times in the said string.


# a=input('enter a string')
# b=''
# c=''

# for i in a:
#     if i not in c:
#       if a.count(i)==1:
#         b+=i
#       else:
#         c+=i
# print(b)
# print(c)
        

# print(b,'the characters that occur multiple times')
# # print(c)


# Write a Python program to find the longest common sub-string from two given strings.
# a=input('enter a string')
# b=input('enter a string')
# max_len=0
# has not taught

# Write a Python program that concatenates uncommon characters from two strings.
# a=input('enter a string')
# b=input('enter a string')

# s1=set(a)
# s2=set(b)

# uncommon=(s1^s2)
# # print(uncommon)
# r=''
# for i in uncommon:
#     r+=i
# print(r)



# Write a Python program to move all spaces to the front of a given string in a single traversal.
# a=input('enter a string')
# spaces=''
# for i in a:
#     if i==' ':
#         spaces+=i
# print(spaces+a.replace(' ',''))

        
# Write a Python program to remove all characters except a specified character from a given string.
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P

# a='exercises'
# exppected_char='e'
# result='' 

# for i in a:
#     if i==exppected_char:
#         result+=i
# print('original string : ',a)
# print('after removing all character expect : ',exppected_char)
# print(result)

# Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
# a=input('enter a string')
# upperc=0
# lowerc=0
# specialc=0
# numericc=0
# for i in a:
#     if i.isupper():
#         upperc+=1
#     elif i.islower():
#         lowerc+=1
#     elif i.isdigit():
#         numericc+=1
#     else:
#         specialc+=1
# print(upperc)
# print(lowerc)
# print(numericc)
# print(specialc)


# 75. Write a Python program to find the smallest window that contains all characters in a given string.
# Click me to see the sample solution

# 76. Write a Python program to count the number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters.
# Click me to see the sample solution

# 77. Write a Python program to count the number of non-empty substrings of a given string.
# Click me to see the sample solution

# Write a Python program to count the number of non-empty substrings of a given string.
# Click me to see the sample solution

#  Write a Python program to count characters at the same position in a given string (lower and uppercase characters) 
# as in the English alphabet.
# a=input('enter a string')
# has not taught


# 79. Write a Python program to find the smallest and largest words in a given string.
# a=input('enter a string')
# b=a.split()
# smallest_wrd=largest_wrd=b[0]
# for i in b:
#     if len(i)<len(smallest_wrd):
#         smallest_wrd=i
#     elif len(i)>len(largest_wrd):
#         largest_wrd=i
# print('smallest word is :' ,smallest_wrd)
# print('largest word is :' ,largest_wrd)


# 80. Write a Python program to count the number of substrings with the same first and last characters in a given string.
# Click me to see the sample solution

# 81. Write a Python program to determine the index of a given string at which a certain substring starts. If the substring is not found in the given string return 'Not found'.


#  Write a Python program to wrap a given string into a paragraph with a given width.
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick
# # brown f ox.

# a="The quick brown fox."
# width=10
# words=a.split()
# currentline=''
# lines=[]

# for i in words:
#     if len(currentline)+len(i)<=width:
#         currentline+=i+' '
#         print(currentline)
#     else:
#         lines.append(currentline.strip())
#         print(lines)
#         currentline=i+' '
#         print(currentline)
# lines.append(currentline.strip())
# # print(lines)
# para=''
# for i in lines:
#     para+=i+'\n'
# print(para)
                     
                     


# write a python program to  swwapcases in a given string
# a='Python Exercises'
# print(a.swapcase())



# 86. Write a Python program to delete all occurrences of a specified character in a given string.
# a=input('enter a string')
# print(a.replace('a',''))


# Write a Python program to find the common values that appear in two given strings
# a=input('enter a string')
# b=input('enter a string')
# r=''
# for i in a:
#     if i in b :
#         r+=i
# print(r)

                     
# 88. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.

        


# s = input("Enter a string: ")

# # Initialize the flags for capital letter, lower case letter, number and minimum length
# has_capital = False
# has_lower = False
# has_number = False
# has_min_length = False

# # Loop through each character in the string
# for c in s:
#   # Check if the character is a capital letter
#   if c.isupper():
#     has_capital = True
#   # Check if the character is a lower case letter
#   if c.islower():
#     has_lower = True
#   # Check if the character is a number
#   if c.isdigit():
#     has_number = True

# # Check if the string has a minimum length of 8
# if len(s) >= 8:
#   has_min_length = True

# # Print the result
# if has_capital and has_lower and has_number and has_min_length:
#   print("The string is valid.")
# else:
#   print("The string is not valid.")        


#  Write a Python program to remove unwanted characters from a given string.
# Sample Output:
# Original String : Pyth*^on Exercis^es
# After removing unwanted characters:
# Python Exercises


# a=input('enter a string')
# b=['@' ,'#','$','^','*']
# for i in b:
#     a=a.replace(i,'')
# print(a)

# Write a Python program to remove duplicate words from a given string.
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution

# a=input('enter a string')
# b=a.split()
# c=''
# for i in b:
#     if i not in c:
#         c+=i+' '
# print(c)


# Write a Python program to convert a given heterogeneous list of scalars into a string.
# Sample Output:
# Original list:
# ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# Convert the heterogeneous list of scalars into a string:
# Red,100,-50,green,w,3,r,12.12,False   

# a= ["Red", 100, -50, "green", "w,3,r", 12.12, False]
# r=''
# for i in range(len(a)):
#     r+=str(a[i])
#     # print(r)
#     if i<(len(a)-1):
#         r+=','
# print(r)

#  Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]


# a=input('enter a string')
# for i in a.split():
#     if i.isnumeric():
#         print(i)

# Write a Python program to decapitalize the first letter of a given string
# a=input('enter a string')
# # print(a.lower())
# print(a[0].lower()+a[1:])

# Write a Python program to split a multi-line string into a list of lines.
# a='the \n camera \n has been \n broken. '.split('\n')
# print(a)        


# Write a Python program to check whether any word in a given string contains duplicate characters or not. Return True or False.
# a=input('enter a string')
# result=True
# for i in a.split():
#     chars=set(i)
#     if len(chars)<len(i):
#         result=False
# print(result)

# Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if the numbers are strings.

# a=input('enter a string')
# b=input('enter a string') 
# if a.isnumeric() and b.isnumeric():
#     c=int(a)
#     d=int(b)
#     r=str(c+d)
#     print('the sum of the string is',r)
# else:
#     print('invalid input .the string must be postive integers')


# Write a Python program to remove punctuation from a given string.
# Sample Output:
# Original text:
# String! With. Punctuation?
# After removing Punctuations from the said string:
# String With Punctuation
# a=input('enter a string')
# b='!.?'
# for i in b:
#     if i in a:
#         a=a.replace(i,'')
# print(a)

# Write a Python program to replace each character of a word of length five and more with a hash character (#).
# a=input('enter a string')
# b=a.split()
# for i in b:
#     if len(i)>=5:
#         a=a.replace(i,'#' *len(i))
# print(a)

# Write a Python program that capitalizes the first letter and lowercases the remaining letters in a given string.
# a=input('enter a string')
# print(a.title())

# Write a Python program to extract and display the name from a given Email address
# a=input('enter a string')
# print(a.split('@')[0])

# Write a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string.
# a=input('enter a string')
# output=''
# for i in range(len(a)):
#     if i==0 or a[i]!=a[i-1]:
#         output+=a[i]
# print(output).

 


# Write a Python program that takes two strings. Count the number of times each string contains the same three letters at the same index.





# Write a Python program that takes a string and returns # on both sides of each element, which are not vowels.
# a=input('enter a string')
# b='aeiou'
# output=''
# for i in a:
#     if i  not in  b:
#        output+='-'+i+'-'
#     else:
#         output+=i
# print(output)    

# Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.
# a=input('enter the start year')
# b=input('enter the end year:')
# a=int(a)
# b=int(b)
# c=0
# for i in range(a,b+1):
#     if i % 4==0 and  (i % 100==0 or i % 400!=0):
#         c+=1
# print(c)


# WRITE A PYTHN PROGRM TO INSERT SPACE BEFORE EVERY CAPITAL LETTER APPEARS IN A GIVEN WRD
# a=input('enetr a string')
# result=''
# for i in a:
#     if i.isupper():
#         result+=' '+i
#     else:
#         result+=i
# print(result)

# write a pythn prgram tjt takes a string and replaces all the chars with their respectve no.s
# has not taught




# Write a Python program to calculate the sum of two numbers given as strings. Return the result in the same string representation.
# Sample Data:
# ( "234242342341", "2432342342") -> "236674684683"
# ( "", "2432342342") -> False ( "1000", "0") -> "1000"
# ( "1000", "10") -> "1010"

# a=input('enter a no')
# b=input('enter a no')
# if not a.isnumeric() or not b.isnumeric():
#     print('False')
# else:
#     a=int(a)
#     b=int(b)
#     sum=str(a+b)
# print(sum)    
# Write a Python program that returns a string sorted alphabetically by the first character of a given string of words
# a=input('enter a string')
# b=a.split()
# c='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# o=[]
# for letter in c:
#     for i in b:
#         if i[0]==letter:
#             o.append(i)
# print(o)
# r=''
# for i in o:
#     r+=i+' '
# print(r)            
        
    #######################   List Exercise   #####################################################


    # Python program to interchange first and last elements in a list

# a=[]
# size=int(input('enter size of list:  '))
# for i in range(size):
#     a.append(input('enter values'))
# i=0
# j=size-1
# t=a[i]
# a[i]=a[j]
# a[j]=t
# print(a)

# Python program to swap two elements in a list

# a=[23,65,19,20]
# pos1=1
# pos2=3
# temp=a[pos1]
# a[pos1]=a[pos2]
# a[pos2]=temp
# print(a)


# Python – Swap elements in String list

# a=['hello','world','python','bing']

# for i in range(len(a)):
#     n=len(a[i] )    
#     newstring=''
#     for j in range(n):
#         if j==0:
#             newstring+=a[i] [n-1]
#         elif j==n-1:
#             newstring+=a[i][0]
#         else:
#             newstring+=a[i][j]
#     a[i]=newstring
# print(a)




    # Python | Ways to find length of list
# a=[12,56,8,9]
# print(len(a))

# Given two numbers, write a Python code to find the Maximum of these two numbers.
# a=[12,34,7]
# max=a[0]

# for i in a:
#     if max<i:
#         max=i
# print(max)

# Given two numbers, write a Python code to find the Minimum of these two numbers
# a=[12,45]
# print(min(12,45))
# Check if an element exists in a list in Python
# a=[1,6,3,5,3,4]
# i=3
# if i in a:
#     print('exist')
# else:
#     print('not exist')

# pythn prgrm to clear list in python
# a=[2,3,5,6,7]
# del a[:]
# # a.clear()
# print(a)
#


# Reversing a List in Python
# a=[2,4,'hy']
# print(a[::-1])
# # a.reverse()
# print(a)

# # Python | Cloning or Copying a list
# a=[1,2,4,3,5,2]
# c=[]
# # b=a.copy()
# # print(b)
# for i in a:
#     c.append(i)
# print(c)

# Given a list in Python and a number x, count the number of occurrences of x in the given list.

# a = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# # print(a.count(10))
# x=10
# count=0
# for i in a:
#     if i==x:
#         count+=1
# print(count)

# # Find sum and average of List in Python
# a=[4, 5, 1, 2, 9, 7, 10, 8]
# sum=0
# count=0
# for i in a:
#     sum+=i
#     count+=1
# print(sum)
# avg=sum/count
# print(avg)

# Python | Sum of number digits in List
# a=[11,2,22]
# l=[]
# for i in a:
#     sum=0
#     while i>0:
#         sum+=i%10
#         i=i//10
#     l.append(sum)
# print(l)
    
# Multiply all numbers in the list in python
# a=[2,3,4,1]
# mul=1
# for i in a:
#     mul*=i
# print(mul)

# Python program to find smallest number in a list
# a=[2,3,1]
# # print(min(a))
# min=a[0]
# for i in a:
#     if i <min:
#         min=i
# print(min)

# Python program to find largest number in a list
# a=[2,1,22,33,1,100,3]
# a.sort()
# print(a[-1])

# Python program to find second largest number in a list
# list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
# # print(max(list1))
# list1=list(set(list1))
# list1.sort()
# print(list1[-2])

# Python program to print even numbers in a list
# a=[1,2,4,365,44]
# b=[]
# for i in a:
#     if i%2==0:
#       b.append(i)
# print(b)

# Python program to print odd numbers in a List
# a= [2,7,5,64,14]
# b=[]
# for i in a:
#     if i%2!=0:
#         b.append(i)
# print(b)
        
# Python program to print all even numbers in a range
# start=4
# stop=14
# b=[]
# for i in range(start,stop+1):
#     if i%2==0:
#         b.append(i)
# print(b)
        
# # Python program to print all odd numbers in a range
# start=1
# stop=9
# for i in range(start,stop+1):
#     if i%2!=0:
#         print(i,end=' ')


# Python program to count Even and Odd numbers in a List
# a=[10, 21, 4, 45, 66, 93, 1]
# counte=0
# counto=0
# for i in a:
#     if i%2==0:
#         counte+=1
#     else:
#         counto+=1
# print(counte, '--even nos count')
# print(counto, '--odd nos count')


# Python program to print positive Numbers in a List

# a=[12, 14, -95, 3]
# for i in a:
#     if i>=0:
#       print('positive no ' ,i)
    
# Python program to print negative numbers in a list
# a= [12, -7, 5, 64, -14]
# for i in a:
#     if i<0:
#         print('negaive no',i)

# Python program to print all positive numbers in a range
# start=-4
# stop=19
# for i in range(start,stop+1):
#     if i>=0:
#         print(i,end=' ')

# Python program to print all negative numbers in a range
# a = -4
# b = 5
# for i in range(a,b+1):
#     if i<0:
#         print(i,end=' ')

# Python program to count positive and negative numbers in a list
# counte=0
# counto=0
# a=[1,3,4,-7,9,-7,-5]
# for i in a:
#     if i>=0:
#         counte+=1
#     else:
#         counto+=1
# print(counte)
# print(counto)
    