import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    global filename 
    filename = filedialog.askopenfilename()
    print(filename)
    bg_img.config(image=tk.PhotoImage(file=filename))
    bg_img.pack()
  
def refresh():
    bg_img.after(200)

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

bg_img = tk.Label(root,image=tk.PhotoImage(file='C:/Users/yuioo/OneDrive - 성균관대학교/1학년 2학기/문제해결과알고리즘(정해선)/러닝페어/space_shade.PNG'))
bg_img.pack()

bg = 'space_shade.png'
root.geometry('1366x768')

#img = 

refresh()
root.mainloop()