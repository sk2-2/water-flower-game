from tkinter import *
import time
import random
from tkinter import messagebox
import threading

root=Tk()
root.geometry("5000x5500")


a=random.randint(7,1000)
pic1=PhotoImage(file="drop.png")
l1=Label(root,image=pic1)
l1.place(x=a,y=0)

b=0

def start():
    t1 = threading.Thread(target=move, )
    t1.start()
def move():
    global b
    for i in range(0,540,6):
        b=b+5
        time.sleep(0.08)
        l1.place(x=a,y=b)



pic2=PhotoImage(file="flower.png")
l2=Label(root,image=pic2)
l2.place(x=550,y=450)

l3=Label(root,text="--------------------------------------------------------------------------------------------=------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
l3.place(x=0,y=600)

l=550
def left():
    global l
    global p
    p=450
    l=l-7
    l2.place(x=l,y=p)
    """t1 = threading.Thread(target=move, )
    t1.start()"""
    if (l==a and p==b):
        messagebox.showinfo("win","you won")
b1=Button(root,text="<<<",command=left)
b1.place(x=500,y=700)

r=550
def right():
    global p
    p=450
    global r
    r=r+5
    l2.place(x=r,y=p)
    """t2 = threading.Thread(target=move, )
    t2.start()"""
    if (r==a and p==b):
        messagebox.showinfo("win","you won")
b2=Button(root,text=">>>",command=right)
b2.place(x=800,y=700)

b3=Button(root,text="START",command=start)
b3.place(x=600,y=700)

root.mainloop()
