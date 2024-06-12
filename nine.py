# Importing tkinter module 
from tkinter import *
# Importing random module
import random
from tkinter import messagebox
 
# Creating a tkinter window
a = Tk() 
 
a.title("Chennai Dhaba")
# Initialize tkinter window with dimensions 300 x 250
a.geometry('300x250')

def clic():
    messagebox.showinfo("dhaba","add one plate tandoori")
    a.destroy

Label(a,text="One plate Tandoori Chicken").pack()

Button(a,text="yes",command=clic).pack()
 
# Creating a Button
btn = Button(a, text = 'No')
btn.pack()
 
# Defining method on click
def Clicked(event):
    x = random.randint(50,250)
    y = random.randint(50,200)
    btn.place(x=x, y=y)
     
     
# bind button
btn.bind("<Button-1>" ,Clicked)
btn.pack()
 
a.mainloop()