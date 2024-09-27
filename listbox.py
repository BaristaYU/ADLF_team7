from tkinter import *

window = Tk()
window.geometry("500x500")

frame = Frame(window)
frame.pack()

listNodes = Listbox(frame, width=20, height=20, font=("Helvetica", 12))
listNodes.pack(side="left", fill="y")

scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.config(command=listNodes.yview)
scrollbar.pack(side="right", fill="y")

listNodes.config(yscrollcommand=scrollbar.set)

for x in range(100):
	listNodes.insert(END, str(x))

window.mainloop()