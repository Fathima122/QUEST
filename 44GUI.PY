# # day 45
# import tkinter as tk
# window=tk.Tk()
# from tkinter import Menu  #menu bar
# menubar=Menu(window)
# filemenu=Menu(menubar)
# # def display():
# #     print('hii')


# # filemenu.add_command(label='New',command=display)
# # filemenu.add_command(label='open')
# # filemenu.add_command(label='save')
# # filemenu.add_separator()
# # filemenu.add_command(label='close')
# menubar.add_cascade(label='File',menu=filemenu)
# window.config(menu=menubar)

# editmenu=Menu(menubar)
# editmenu.add_command(label='aa')
# # editmenu.add_command(label='bb')
# # menubar.add_cascade(label='edit',menu=editmenu)

# # window.config(menu=menubar)
# window.mainloop()


# # pack

# # vertical positioning with pack

# import tkinter as tk
# root=tk.Tk()


# test=tk.Label(root,text='red',bg=-'red',fg='white')
# test.pack(side=tk.RIGHT)
# test=tk.Label(root,text='green',bg=-'green',fg='white')
# test.pack(side=tk.LEFT)
# test=tk.Label(root,text='hii',bg=-'purple',fg='white')
# test.pack(side=tk.BOTTOM)

# tk.mainloop()
# # # side by side positioning with pack

# import tkinter as tk
# root=tk.Tk()

# test=tk.Label(root,text='red',bg='red',fg='white')
# test.pack(padx=25,pady=15,side=tk.LEFT)


# test=tk.Label(root,text='red',bg='red',fg='white')
# test.pack(padx=5,pady=20,side=tk.LEFT)


# # test=tk.Label(root,text='red',bg='red',fg='white')
# # test.pack(padx=25,pady=15,side=tk.LEFT)

# # tk.Label(root,text='purple',bg='purple',fg='white').place(padx=5, pady=20, side=tk.LEFT)
# root.mainloop()

# from tkinter import *
# root=Tk()

# root.geometry('250x200+550+100')
# Label(root,text='aaaa',bg='#FFFF00',
#       fg='red').place(x=400,y=50)

# # Label(root,text='Position 2 : x=50, y=40',bg='#3300cc',fg='white').place(x=50,y=40)
# # Label(root,text='Position 3 : x=75,y=80',bg='#FF0099',fg='white').place(x=70,y=67)
# # Label(root,text='purple',bg='blue',fg='white').grid(row=12,column=3)
# # Label(root,text='purple',bg='purple',fg='white').place(padx=5, pady=20, side=LEFT)
# root.mainloop()



# import tkinter as tk
# import tkinter.ttk as ttk



# root=tk.Tk()
# root.title('place')
# root.geometry('400x600')
# a=tk.Label(text='welcome',bg='red',fg='black',height=67,width=39)
# a.place(x=100,y=200,width=300,height=50)
# b=ttk.Label(root,text='ttklabel',background='red')
# b.place(relx=0.2,rely=0.1,relwidth=0.4,relheight=0.5)
# c=ttk.Label(root,text='ttklabel2',background='red')
# c.place(x=80,y=60,width=160,height=300)
# btn=ttk.Button(text='button')
# btn.place(relx=1,rely=1)
# tk.mainloop()



# import tkinter as tk
# import tkinter.ttk as ttk

# window=tk.Tk()

# label1=tk.Label(text='label1',bg='yellow',fg='red')
# label1.pack(side=tk.TOP)
# label1.pack(side=tk.BOTTOM)
# label1.pack(side=tk.LEFT)
# label1.pack(side=tk.RIGHT)
# label1.pack(padx=34,pady=150,side=tk.RIGHT)
# label1.place(x=20,y=56)






# window.mainloop()



# import tkinter as tk
# import tkinter.ttk as ttk

# from tkinter import Menu

# window=tk.Tk()
# menu=Menu(window)
# fileu=Menu(menu)
# editmenu=Menu(menu)

# def fn():
#     print('hello')

# fileu.add_command(label='new',command=fn)
# fileu.add_command(label='open')
# fileu.add_command(label='save')
# fileu.add_separator()
# fileu.add_command(label='close')
# menu.add_cascade(label='file',menu=fileu)

# editmenu.add_command(label='aa')
# menu.add_cascade(label='edit',menu=editmenu)


# window.config(menu=menu)
# window.mainloop()











