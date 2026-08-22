from tkinter import *

root = Tk()

# ---------------- BACKEND ----------------

def click(value):
    ent.insert(END, value)

def clear_all():
    ent.delete(0, END)

def clear_one():
    current = ent.get()
    ent.delete(0, END)
    ent.insert(END, current[:-1])

def calculate():
    try:
        expression = ent.get()
        expression = expression.replace("x", "*")
        result = eval(expression)

        ent.delete(0, END)
        ent.insert(END, result)

    except:
        ent.delete(0, END)
        ent.insert(END, "Error")


# ---------------- FRONTEND ----------------

root.geometry("350x550")
root.title("R-calculator")
root.minsize(350, 550)
root.maxsize(350, 550)

lb1 = Label(root, text="R-calculator",
            font=("arial",20,"bold"),
            bg="green", width=22, fg="white")
lb1.pack()

ent = Entry(root, font=("arial",20,"bold"))
ent.place(x=5,y=45,width=336,height=60)


# AC
bt1 = Button(root, text="AC", bg="red",
             font=("arial",20,"bold"),
             fg="white", command=clear_all)
bt1.place(x=5,y=120,height=80,width=80)


# CE
bt2 = Button(root, text="CE", bg="red",
             font=("arial",20,"bold"),
             fg="white", command=clear_one)
bt2.place(x=90,y=120,height=80,width=80)


# %
bt3 = Button(root, text="%", bg="gray",
             font=("arial",20,"bold"),
             command=lambda: click("%"))
bt3.place(x=175,y=120,height=80,width=80)


# +
bt4 = Button(root, text="+", bg="gray",
             font=("arial",20,"bold"),
             command=lambda: click("+"))
bt4.place(x=260,y=120,height=80,width=80)


# 7
bt5 = Button(root, text="7",
             font=("arial",20,"bold"),
             command=lambda: click("7"))
bt5.place(x=5,y=205,height=80,width=80)


# 8
bt6 = Button(root, text="8",
             font=("arial",20,"bold"),
             command=lambda: click("8"))
bt6.place(x=90,y=205,height=80,width=80)


# 9
bt7 = Button(root, text="9",
             font=("arial",20,"bold"),
             command=lambda: click("9"))
bt7.place(x=175,y=205,height=80,width=80)


# x
bt8 = Button(root, text="x", bg="red",
             font=("arial",20,"bold"),
             command=lambda: click("x"))
bt8.place(x=260,y=205,height=80,width=80)


# 4
bt9 = Button(root, text="4",
             font=("arial",20,"bold"),
             command=lambda: click("4"))
bt9.place(x=5,y=290,height=80,width=80)


# 5
bt10 = Button(root, text="5",
              font=("arial",20,"bold"),
              command=lambda: click("5"))
bt10.place(x=90,y=290,height=80,width=80)


# 6
bt11 = Button(root, text="6",
              font=("arial",20,"bold"),
              command=lambda: click("6"))
bt11.place(x=175,y=290,height=80,width=80)


# -
bt12 = Button(root, text="-", bg="gray",
              font=("arial",20,"bold"),
              command=lambda: click("-"))
bt12.place(x=260,y=290,height=80,width=80)


# 1
bt13 = Button(root, text="1",
              font=("arial",20,"bold"),
              command=lambda: click("1"))
bt13.place(x=5,y=375,height=80,width=80)


# 2
bt14 = Button(root, text="2",
              font=("arial",20,"bold"),
              command=lambda: click("2"))
bt14.place(x=90,y=375,height=80,width=80)


# 3
bt15 = Button(root, text="3",
              font=("arial",20,"bold"),
              command=lambda: click("3"))
bt15.place(x=175,y=375,height=80,width=80)


# /
bt16 = Button(root, text="/", bg="gray",
              font=("arial",20,"bold"),
              command=lambda: click("/"))
bt16.place(x=260,y=375,height=80,width=80)


# 0
bt17 = Button(root, text="0",
              font=("arial",20,"bold"),
              command=lambda: click("0"))
bt17.place(x=5,y=460,height=80,width=80)


# 00
bt18 = Button(root, text="00",
              font=("arial",20,"bold"),
              command=lambda: click("00"))
bt18.place(x=90,y=460,height=80,width=80)


# =
bt19 = Button(root, text="=", bg="green",
              font=("arial",20,"bold"),
              command=calculate)
bt19.place(x=175,y=460,height=80,width=80)


# .
bt20 = Button(root, text=".", bg="gray",
              font=("arial",20,"bold"),
              command=lambda: click("."))
bt20.place(x=260,y=460,height=80,width=80)


root.mainloop()