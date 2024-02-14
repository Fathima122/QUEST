# #                                 radiobbtn


# import tkinter as tk

# import tkinter.ttk as ttk

# # from tkinter import scrolledtext

# window=tk.Tk()
# window.geometry('500x500')

# selected=tk.IntVar()
# selected1=tk.StringVar()

# selected1.set(0)



# rad1=tk.Radiobutton(window,text='first',variable=selected,value=1)
# rad1.grid(row=1,column=1)


# rad2=tk.Radiobutton(window,text='second',variable=selected,value=2)
# rad2.grid(row=1,column=2)


# rad3=tk.Radiobutton(window,text='third',variable=selected1,value='3')
# rad3.grid(row=2,column=1)

# rad4=tk.Radiobutton(window,text='four',variable=selected1,value='six')
# rad4.grid(row=2,column=2)


# def display():
#     print(selected.get())
#     print(selected1.get())


# btn=tk.Button(text='click me',fg='green',command=display)
# btn.grid(row=3,column=1)

# # st=scrolledtext.ScrolledText(window,width=20,height=10)
# # st.grid(row=1,column=3)

# # def display():
# #     # a=st.get('1.0')
# #     print(a)
#     # st.insert('1.2',77)
#     # st.delete('1.0')


# # btn=ttk.Button(text='click me',command=display)
# # btn.grid(row=2,column=3)

# window.mainloop()


# # #                                                               messagebox
# import tkinter as tk

# # import tkinter.ttk as ttk

# window=tk.Tk()


# window.geometry('500x500')



# from tkinter import messagebox

# def display():
#     # messagebox.showinfo('title','content')
#     messagebox.showwarning('title','content')
#     # messagebox.showerror('title','content')

# btn=tk.Button(text='click',command=display)
# btn.grid(row=1,column=2)

# window.mainloop()




#                                  progress bar

import tkinter as tk

import tkinter.ttk as ttk

from tkinter.ttk import Progressbar

window=tk.Tk()
window.geometry('500x500')


bar=Progressbar(window,length=200)
bar['value']=50
bar.grid(row=1,column=2)

window.mainloop() 







import tkinter as tk

import tkinter.ttk as ttk

window=tk.Tk()


























txt=ttk.Entry(width=50)
txt.grid(row=0,columnspan=34)





def one():
    chk()
    txt.insert(tk.END,'1')



def two():
    chk()
    txt.insert(tk.END,'2')

def three():
    chk()
    txt.insert(tk.END,'3')


def four():
    chk()
    txt.insert(tk.END,'4')

def five():
    chk()
    txt.insert(tk.END,'5')

def six():
    chk()
    txt.insert(tk.END,'6')

def seven():
    chk()
    txt.insert(tk.END,'7')

def eight():
    chk()
    txt.insert(tk.END,'8')

def nine():
    chk()
    txt.insert(tk.END,'9')

def zero():
    chk()
    txt.insert(tk.END,'0')

def dzero():
    txt.insert(tk.END,'00')

def point():
    txt.insert(tk.END,'.')

def plus():
    op()
    txt.insert(tk.END,'+')

def minus():
    op()
    txt.insert(tk.END,'-')


def mul():

    op()
    txt.insert(tk.END,'*')


def div():
    op()
    txt.insert(tk.END,'/')


def per():
    txt.insert(tk.END,'%')


def eq():
    a=txt.get()
    ans=eval(a)
    txt.delete(0,tk.END)
    txt.insert(tk.END,ans)

def clear():
    txt.delete(0,tk.END)

def back():
    d=txt.get()
    txt.delete(len(d)-1)
 
        

def op():
    a=txt.get()

    if a[-1] in '+-*/':
        txt.delete(len(a)-1)

def chk():
    n=txt.get()
    if len(n)==1 and n[0]=='0':
        txt.delete(0,tk.END)

btn=ttk.Button(text='<--',command=back )
btn.grid(row=1,column=2)

btn=ttk.Button(text='C',command=clear )
btn.grid(row=1,column=0)


btn=tk.Button(text='=',bg='green',width=9,command=eq)
btn.grid(row=5,column=3)


btn=ttk.Button(text='%',command=per)
btn.grid(row=1,column=1)

btn=ttk.Button(text='/',command=div)
btn.grid(row=1,column=3)

btn=ttk.Button(text='x',command=mul)
btn.grid(row=4,column=3)

btn=ttk.Button(text='-',command=minus)
btn.grid(row=3,column=3)

btn=ttk.Button(text='+',command=plus)
btn.grid(row=2,column=3)


btn=ttk.Button(text='.',command=point)
btn.grid(row=5,column=2)


btnzz=ttk.Button(text='00',command=dzero)
btnzz.grid(row=5,column=0)

btnz=ttk.Button(text='0',command=zero)
btnz.grid(row=5,column=1)

btn9=ttk.Button(text='9',command=nine)
btn9.grid(row=4,column=2)


btn8=ttk.Button(text='8',command=eight)
btn8.grid(row=4,column=1)


btn7=ttk.Button(text='7',command=seven)
btn7.grid(row=4,column=0)



btn6=ttk.Button(text='6',command=six)
btn6.grid(row=3,column=2)

btn5=ttk.Button(text='5',command=five)
btn5.grid(row=3,column=1)

btn4=ttk.Button(text='4',command=four)
btn4.grid(row=3,column=0)

btn3=ttk.Button(text='3',command=three)
btn3.grid(row=2,column=2)


btn2=ttk.Button(text='2',command=two)
btn2.grid(row=2,column=1)


btn1=ttk.Button(text='1',command=one)
btn1.grid(row=2,column=0)




window.mainloop()





# r

# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('300x500')

# selected=tk.IntVar()
# selected1=tk.StringVar()
# # selected.set(0)
# # selected1.set(0)




# rad1=tk.Radiobutton(window,text='first',fg='red',width=20,var=selected,value=1)
# rad1.grid(row=1,column=0)

# rad2=ttk.Radiobutton(window,text='second',width=20,var=selected1,value='three')
# rad2.grid(row=1,column=1)


# def display():
#     print(selected.get())
#     print(selected1.get())
    

# btn=ttk.Button(text='click me',command=display)
# btn.grid(row=2,column=0)

# window.mainloop()



# import tkinter as tk
# import tkinter.ttk as ttk

# window=tk.Tk()

# from tkinter import messagebox

# def display():
#     messagebox.showinfo('title','content')

# btn=tk.Button(text='click me',height=7,command=display)
# btn.grid(row=1,column=1)

# btn=ttk.Button(text='click me',command=display)
# btn.grid(row=1,column=3)

# window.mainloop()

# import tkinter as tk
# from tkinter.ttk import Progressbar

# window=tk.Tk()

# bar=Progressbar(window,length=50)
# bar['value']=50
# bar.grid(row=1,column=1)

# window.mainloop()