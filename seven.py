# ''''''# import tkinter
# # tkinter._test()
# #import module
# from tkinter import *
# #create a window using a variable
# a = Tk()
# #root window title and dimensions
# a.title("day seven game")


# b = Label(a, text="Google")
# b.grid()

# d = Entry(a,width=10)
# d.grid(column=1,row=0)

# def clicked():
#     b.configure(text="Just now Clicked")

# c = Button(a, text ="Search",fg = "purple",command=clicked)

# c.grid(column=2,row=0)

# #set geometry functions(width * height)
# a.geometry("350x300")
# #all widgets will be here
# #execute tkinter
# a.mainloop()


'''
XOX Game
9 buttons
9 buttons no text only blank
geometer 500 x500
messagebox
player 1
player 2
'''

from tkinter import *
from tkinter import ttk

a = Tk()

a.geometry("500x380")
a.title("XOX Game")

but = ttk.Button(a,text=' ',command=lambda:butpress(1))
but.grid(column=0,row=0,ipadx=50,ipady=50)

but1 = ttk.Button(a,text=' ',command=lambda:butpress(2))
but1.grid(column=1,row=0,ipadx=50,ipady=50)

but2 = ttk.Button(a,text=' ',command=lambda:butpress(3))
but2.grid(column=2,row=0,ipadx=50,ipady=50)

but3 = ttk.Button(a,text=' ',command=lambda:butpress(4))
but3.grid(column=0,row=1,ipadx=50,ipady=50)

but4 = ttk.Button(a,text=' ',command=lambda:butpress(5))
but4.grid(column=1,row=1,ipadx=50,ipady=50)

but5 = ttk.Button(a,text=' ',command=lambda:butpress(6))
but5.grid(column=2,row=1,ipadx=50,ipady=50)

but6 = ttk.Button(a,text=' ',command=lambda:butpress(7))
but6.grid(column=0,row=2,ipadx=50,ipady=50)

but7 = ttk.Button(a,text=' ',command=lambda:butpress(8))
but7.grid(column=1,row=2,ipadx=50,ipady=50)

but8 = ttk.Button(a,text=' ',command=lambda:butpress(9))
but8.grid(column=2,row=2,ipadx=50,ipady=50)


player = 1 
def butpress(butnumber):
    global player


    if butnumber == 1 and player ==1:
        but.config(text="x")
        player = 2

    elif butnumber == 2 and player == 1:
        but.config(text="x")
        player=2

    elif butnumber == 3 and player == 1:
        but.config(text="x")
        player=2

    elif butnumber == 4 and player == 1:
        but.config(text="x")
        player=2
    
    elif butnumber == 5 and player == 1:
        but.config(text="x")
        player=2

    elif butnumber == 6 and player == 1:
        but.config(text="x")
        player=2

    elif butnumber == 7 and player == 1:
        but.config(text="x")
        player=2

    elif butnumber == 8 and player == 1:
        but.config(text="x")
        player=2

    elif butnumber == 9 and player == 1:
        but.config(text="x")
        player=2
a.mainloop()