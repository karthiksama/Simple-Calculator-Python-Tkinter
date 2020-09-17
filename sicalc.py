from tkinter import *

exp=""

def press(num):
 global exp
 exp=exp+str(num)
 equation.set(exp)

def equal():
 try:
    global exp
    total=str(eval(exp))
    equation.set(total)
    exp=''
 except:
    equation.set('error')
    exp=''

def clear():
 global exp
 exp=''
 equation.set('')



p=Tk()

equation=StringVar()
e0=Entry(p,textvariable=equation)

e0.place(x=80,y=180)
equation.set('0')

p.geometry('300x300')

b1=Button(p,text='1',command=lambda:press(1),fg='red',bg='yellow').grid(row=0,column=0)
b2=Button(p,text='2',command=lambda:press(2),fg='red',bg='yellow').grid(row=0,column=1)
b3=Button(p,text='3',command=lambda:press(3),fg='red',bg='yellow').grid(row=0,column=2)
b4=Button(p,text='4',command=lambda:press(4),fg='red',bg='yellow').grid(row=1,column=0)
b5=Button(p,text='5',command=lambda:press(5),fg='red',bg='yellow').grid(row=1,column=1)
b6=Button(p,text='6',command=lambda:press(6),fg='red',bg='yellow').grid(row=1,column=2)
b7=Button(p,text='7',command=lambda:press(7),fg='red',bg='yellow').grid(row=2,column=0)
b8=Button(p,text='8',command=lambda:press(8),fg='red',bg='yellow').grid(row=2,column=1)
b9=Button(p,text='9',command=lambda:press(9),fg='red',bg='yellow').grid(row=2,column=2)
b0=Button(p,text='0',command=lambda:press(0),fg='red',bg='yellow').grid(row=3,column=0)


o1=Button(p,text='+',command=lambda:press('+'),fg='blue').grid(row=0,column=4)
o2=Button(p,text='-',command=lambda:press('-'),fg='blue').grid(row=1,column=4)
o3=Button(p,text='*',command=lambda:press('*'),fg='blue').grid(row=2,column=4)
o4=Button(p,text='/',command=lambda:press('/'),fg='blue').grid(row=3,column=4)

l1=Button(p,text='c',command=lambda:clear(),fg='green').grid(row=3,column=1)
l2=Button(p,text='.',command=lambda:press('.'),fg='green').grid(row=3,column=2)
l3=Button(p,text='=',command=lambda:equal(),fg='black').grid(row=4,column=0)


p.mainloop()
