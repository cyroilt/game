from tkinter import*
from pcloudAPI import*
from ttkbootstrap import Style
from sys import*
from os import *
from tkinter import ttk
from win10toast import ToastNotifier
a=Tk()

import server


def login1():
    q1=Tk()
    label1=ttk.Label(q1,text='write e-mail or nickname',style='primary.Label')
    style = Style(theme='darkrest-sand', themes_file='ttkbootstrap_themes.json',master=q1)
    label1.pack()
    e1=Entry(q1)
    e1.pack()
    label3=Label(q1,text='write password')
    label3.pack()
    e3=Entry(q1)
    e3.pack()
    def p():
        pcloud.login('alqservru@gmail.com','ur1IAbg1Kt6Xp5')
        aaa=login(e1.get(),e3.get())
        print(aaa)
        if aaa!='password_incorrect':
            server.fjs(True)
        a.destroy()
        q1.destroy()
        toaster = ToastNotifier()
        toaster.show_toast("Tribe settlers",
        "You are successully joined",
        icon_path=None,
        duration=10)
        import module1_1
    b=Button(q1,text='ok',command=p)
    b.pack()
def newaccount():
    q1=Tk()

    label1=Label(q1,text='write e-mail')
    label1.pack()
    e1=Entry(q1)
    e1.pack()
    err=Label(q1,text='',fg='red')
    err.pack()
    label2=Label(q1,text='write nickname')
    label2.pack()
    e2=Entry(q1)
    e2.pack()


    label3=Label(q1,text='write password')
    label3.pack()

    e3=Entry(q1)
    e3.pack()
    err2=Label(q1,text='',fg='red')
    err2.pack()
    def p():
        aq=e1.get()
        if aq.find('@')!=-1 and aq.find('.')!=-1:
            err.configure(text='')
            pcloud.login('alqservru@gmail.com','ur1IAbg1Kt6Xp5')
            print(new_player(e2.get(),e1.get(),e3.get()))
            server.fjs(False)
            a.destroy()
            q1.destroy()
            toaster = ToastNotifier()
            toaster.show_toast("Tribe settlers",
            "You are successully created an account",
            icon_path=None,
            duration=10)
            import module1_1
        elif aq.find('@')==-1:
            err.configure(text='email should have @ symbol')
        else:
            err.configure(text='email should have . symbol')
    b=Button(q1,text='create',command=p)
    b.pack()
q=Button(a,text='New account',command=newaccount)
q.pack()
w=Button(a,text='Log in',command=login1)
w.pack()
mainloop()