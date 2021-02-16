from tkinter import *
root=Tk()
root.geometry('500x500')
def show():
    e3.insert(0,e1.get()+" "+e2.get())



def quit():
    root.destroy()


l1=Label(root,text="first name")
l2=Label(root,text="last name")
l3=Label(root,text="u typed")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
b1=Button(root,text="show",command=show)
b2=Button(root,text="quit",command=quit)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=4,column=0)
root.mainloop()


