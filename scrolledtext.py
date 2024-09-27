from tkinter import *

mbox = Tk()
mbox.title('쪽지함')
mbox.geometry('500x400')

frame = Frame(mbox)
frame.pack()

textbox = Text(frame, width=38, height=15, font=("맑은 고딕", 12))
scrollbar = Scrollbar(frame, orient="vertical",command=textbox.yview)
textbox.configure(yscrollcommand=scrollbar.set)

textbox.pack(side="left",fill="y")
scrollbar.pack(side="right", fill="y")

def mailupdate():
    pos = textbox.yview()
    print('scroll 위치:',textbox.yview())
    textbox.delete("1.0",END) #쪽지함 초기화

    for j in range(1,99):
        textbox.insert(END, str(j)+"\n")

    textbox.yview(MOVETO,pos[0])
    textbox.after(500,mailupdate)


mailupdate()
mbox.mainloop()