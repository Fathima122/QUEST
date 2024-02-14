import re
# txt='The rain is spain'
# xe=re.findall('ai',txt)
# print(xe)
# txt='The rain is spain'
# xe=re.search('ai',txt)
# print(xe)
# print(xe.start())

# # []=a set of characters '[a-m]'
# txt='The raIn in Spain'
# #                                                          Find all lower case chrCTERS LPHABETICALLY BETWEEN 'A' AND 'M':
# x=re.findall('[a-i]',txt)
# print(x)

# SUBSTITUTE
# txt='The rain is spain'
# print(txt) 
# x=re.sub('\s','9',txt)
# x=re.sub('\s','9',txt,12)
# print(x)

# txt='Th5e ra20in in1 Spain'
# print(txt)
# x=re.findall('[0123]',txt)
# print(x)


# ^                                            startswith
# txt='The rain in Spain'
# x=re.findall('^The',txt)
# print(x)
# if x:
#     print('yes ')
# else:
#     print('no match')

# txt='The rain in Spain'
# x=re.findall('[^arn]',txt)
# print(x)


# #                                                       $ends with

# txt='hello world'
# x=re.findall('d$',txt)
# # print(x)
# if x:
#     print('yes ,the string ends with world')
# else:
#     print('no match')

# txt='The rain in Spa#indfh'
# x=re.search(r'\bS\w+',txt)
# print(x)
# print(x.start())
# print(x.span()) 
# print(x.string)
# print(x.group())


# txt='The rain in  Spain falls mainly in the plain'
# #                                check if the string contains 'a' followed by exactly 2 'l ' characters
# x=re.findall('al{2}',txt)
# print(x)

# txt='The rain in Spain'
# x=re.findall('\AThe',txt)
# print(x)

# \d returns a match whre the string  contains digits

#  \D  returns a match where the string dows not contain digits(including space,special characters)
#  \s returns a match where a string contains white space
# \S returns a match where the string does not contain  a whte space character
# \W returns a match where the string does not contain any word characters
# # \Z returns a match if the specified chars are at the end of of the string
# import tkinter as tk
# import tkinter.ttk as ttk
# import re
# from tkinter import messagebox
# window=tk.Tk()
# title=tk.Label(text='Registration Form',height=2)
# title.grid(row=1,column=10)

# window.geometry('500x300')

# def name_check():
#     a=entry1.get()
#     b=re.findall('\D')
#     c=re.findall('[@#$%()*^&]')
#     if b!=[] and a not in c:
         


# def n():
#     a=entry1.get()
#     for i in a:
#         if i.isalpha() and ' ' in a:
#              e()
#     else:
#         messagebox.showerror('title','content')

def e():
    b=entry2.get()
    if '@' in b and '.com' or '.in' in b:
        print(';')
    else:
        messagebox.showerror('title','content')



label1=ttk.Label(text='Name:',foreground='black')
label1.grid(row=6,column=0)
entry1=tk.Entry()
entry1.grid(row=6,column=5)

label2=tk.Label(text='Email:',foreground='black',height=4)
label2.grid(row=8,column=0)
entry2=ttk.Entry()
entry2.grid(row=8,column=5 )

label3=ttk.Label(text='password:',foreground='black')
label3.grid(row=10,column=0)
entry4=ttk.Entry()
entry4.grid(row=10,column=5) 

label4=tk.Label(text='Confirm Password:',fg='black',height=4)
label4.grid(row=12,column=0)
entry5=ttk.Entry()
entry5.grid(row=12,column=5)



btn=ttk.Button(text='Submit')
btn.grid(row=14,column=10)





window.mainloop()