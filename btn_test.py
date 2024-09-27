from tkinter import *

window = Tk()
window.geometry("500x500")

btn = Button(window,text='txt' ,overrelief='sunken')
btn.pack()

def btnchkr():
    print(btn)

btn.bind("<Enter>",btnchkr)

window.mainloop()