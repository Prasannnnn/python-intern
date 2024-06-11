'''
QR Code Generate
Libraries:
---> pip install qrcode
'''

from tkinter import *
import qrcode

a = Tk()
a.title("Qr Code Generate")
a.geometry("1000x600")
a.config(bg="light blue")


#generate QR code

def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("qrcode/"+str(name)+".png")

#show the QR Code
    global Image
    Image=PhotoImage(file="qrcode/"+str(name)+".png")
    b.config(image=Image)



b = Label(a,bg="yellow")
b.pack(padx=50,pady=10,side=RIGHT)

Label(a,text="Title",fg="white",bg="black",font=15).place(x=50,y=170)

title = Entry(a,width=13,font="arial 25")
title.place(x=50,y=200)

entry =Entry(a,width=20,font="arial 15")
entry.place(x=50,y=250)

Button(a,text="Generate",width=20,height=2,bg="blue",fg="white",command=generate).place(x=50,y=300)
a.mainloop()
