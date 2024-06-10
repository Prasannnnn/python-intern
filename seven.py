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
def butpress(ButtonNumber):
    global player

    if ButtonNumber == 1 and player==1:
        but.config(text='X')
        player=2

    elif ButtonNumber ==1 and player==2:
        but.config(text='O')
        player = 1

    elif ButtonNumber == 2 and player==1:
        but1.config(text='X')
        player = 2

    elif ButtonNumber ==2 and player==2:
        but1.config(text='O')
        player = 1
    
    elif ButtonNumber == 3 and player==1:
        but2.config(text='X')
        player = 2

    elif ButtonNumber ==3 and player==2:
        but2.config(text='O')
        player = 1

    elif ButtonNumber == 4 and player==1:
        but3.config(text='X')
        player = 2

    elif ButtonNumber ==4 and player==2:
        but3.config(text='O')
        player = 1

    elif ButtonNumber == 5 and player==1:
        but4.config(text='X')
        player = 2

    elif ButtonNumber ==5 and player==2:
        but4.config(text='O')
        player = 1
    
    elif ButtonNumber == 6 and player==1:
        but5.config(text='X')
        player = 2

    elif ButtonNumber ==6 and player==2:
        but5.config(text='O')
        player = 1
    
    elif ButtonNumber == 7 and player==1:
        but6.config(text='X')
        player = 2
    
    elif ButtonNumber == 7 and player==2:
        but6.config(text='O')
        player = 1

    elif ButtonNumber == 8 and player==1:
        but7.config(text='X')
        player = 2

    elif ButtonNumber ==8 and player==2:
        but7.config(text='O')
        player = 1

    elif ButtonNumber == 9 and player==1:
        but8.config(text='X')
        player = 2

    elif ButtonNumber ==9 and player==2:
        but8.config(text='O')
        player = 1


a.mainloop()