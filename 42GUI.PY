# #                                                                 THEMED WIDGETS
# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('200x500')


# btn=tk.Button(text='show',bg='green')
# btn.grid(row=1,column=1)

# btn=ttk.Button(text='show',bg='red')
# btn.grid(row=4,column=1)     error


# btn=tk.Label(text='show',bg='green')
# btn.grid(row=1,column=1)

# btn1=ttk.Label(text='show',bg='red')
# btn1.grid(row=4,column=1)
#  errroe bf ,fg


# btn=ttk.Label(text='show',background='red',width=23)
# btn.grid(row=4,column=1)     


# txt1=tk.Text()
# txt1.grid(row=0,column=0)    # multiplelines

# def display():
#     s=txt1.get('2.0',tk.END)
#     print(s)
#     # txt1.insert('2.1','999')
#     txt1.delete('1.2',tk.END)

# btn=tk.Button(text='click me',command=display)
# btn.grid(row=1,column=1)


# window.mainloop()


# #                                                            combobox


# import tkinter as tk

# import tkinter.ttk as ttk





# window=tk.Tk()
# window.geometry('200x500')




# n=tk.StringVar()

# place=ttk.Combobox(window,width=20,textvariable=n,foreground='green')
# place.grid(row=0,column=1)


# place['values']=('ernklm','kollam','kochi')
# place.current(0)

# def display():
#     p=place.get()
#     print(p)



# btn=ttk.Button(text='click me',command=display)
# btn.grid(row=1,column=1)

# window.mainloop()

#                                        checkbox



# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('200x500')


# cbool=tk.BooleanVar()
# cbool.set(True)

# cbool=tk.IntVar()
# cbool.set(7)



# chk=tk.Checkbutton(window,text='malayalam')
# chk.grid(row=1,column=1)


# chk=ttk.Checkbutton(window,text='malayalam',var=cbool)
# chk.grid(row=1,column=1)


# def display():
#     # a=chk.state()
#     a=chk.instate(['selected'])
#     print(a)

# btn=ttk.Button(text='click me',command=display)
# btn.grid(row=2,column=1)


# window.mainloop()




# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('500x700')

# # def display():
#     d=c.get()
#     print(d)
#     # c.insert(2,'gdjk')
#     e=c1.get()
#     print(e)

#     f=c2.get('1.2',tk.END)
#     print(f)
#     c2.insert('2.1','and')
#     c2.insert(tk.end,'and')
#     c2.delete('1.5')



# btn=tk.Button(text='click me',bg='red',fg='green',command=display)
# btn.grid(row=0,column=0)

# btn=ttk.Button(text='show me',background='red',foreground='green')
# btn.grid(row=0,column=1)

# a=tk.Label(text='hy',bg='green',fg='red',height=67)
# a.grid(row=0,column=2)

# a=ttk.Label(text='hello',background='green',foreground='red')
# a.grid(row=0,column=3)

# c=tk.Entry(bg='yellow')
# c.grid(row=0,column=4)[7yh65f432q1]

# c=ttk.Entry(foreground='red')
# c.grid(row=0,column=5)


# c1=tk.Entry(bg='yellow')
# c1.grid(row=0,column=4)

# c2=tk.Text(bg='yellow',height=89)
# c2.grid(row=0,column=6)

# window.mainloop()



# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('500x500')

# place=ttk.Combobox(width=30)
# place.grid(row=0,column=0)

# place['values']=('ernklm','kochi')
# place.current(1)


# def display():
#     p=place.get()
#     print(p)

# # btn=tk.Button(text='click me',command=display)
# # btn.grid(row=1,column=1)

# # btn=ttk.Button(text='click me',command=display)
# # btn.grid(row=1,column=1)


# window.mainloop()





# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('500x500')

# cbool=tk.BooleanVar()
# cbool.set(True)

# # cbool=tk.IntVar()
# # cbool.set(7)


# # chk=tk.Checkbutton(window,text='malayalam',fg='red',bg='green',width=34,height=10)
# # chk.grid(row=0,column=0)

# chk=ttk.Checkbutton(window,text='malayalam',var=cbool,width=30)
# chk.grid(row=0,column=0)

# def display():
#     # a=chk.state()
#     a=chk.instate(['selected'])
#     print(a)

# btn=ttk.Button(text='click me',command=display)
# btn.grid(row=0,column=1)

# btn=tk.Button(text='click me',fg='green',command=display)
# btn.grid(row=0,column=1)

# window.mainloop()