from tkinter import *

post = Tk()
post.title("님의 이차원 보관소")
post.geometry('500x400')

tagvar = IntVar()
placevar = IntVar()

def lost():
    place1_btn.place_forget()
    place2_btn.place_forget()
    place3_btn.place_forget()
    weetak_lab.place_forget()

    reward_lab.place(x=150,y=220)
    reward_ent.place(x=250,y=220)
    saryeh_lab.place(x=150,y=250)
    
def find():
    reward_lab.place_forget()
    reward_ent.place_forget()
    saryeh_lab.place_forget()

    place1_btn.place(x=150,y=220)
    place2_btn.place(x=250,y=220)
    place3_btn.place(x=340,y=220)
    weetak_lab.place(x=150,y=250)
    place1_btn.select()

lost_btn = Radiobutton(post,text='찾습니다',value=0,variable=tagvar,command=lost)
lost_btn.place(x=150,y=30)
find_btn = Radiobutton(post,text='주웠어요',value=1,variable=tagvar,command=find)
find_btn.place(x=250,y=30)

lost_btn.select()

title_lab = Label(post, text='제목 (필수)',font=('맑은 고딕', 10))
title_lab.place(x=150,y=70)
title_ent = Entry(post)
title_ent.place(x=250,y=70)

info_lab = Label(post, text='세부사항 (필수)',font=('맑은 고딕', 10))
info_lab.place(x=150,y=120)
info_ent = Entry(post)
info_ent.place(x=250,y=120)

tel_lab = Label(post, text='연락처 (선택)',font=('맑은 고딕', 10))
tel_lab.place(x=150,y=170)
tel_ent = Entry(post)
tel_ent.place(x=250,y=170)

reward_lab = Label(post, text='사례 (선택)',font=('맑은 고딕', 10))
reward_ent = Entry(post)
saryeh_lab = Label(post,text="* 사례가 있을 시 글 제목이 강조됩니다.")

place1_btn = Radiobutton(post,text='원위치',value=0,variable=placevar,font=('맑은 고딕', 12))
place2_btn = Radiobutton(post,text='위탁',value=1,variable=placevar,font=('맑은 고딕', 12))
place3_btn = Radiobutton(post,text='취득',value=2,variable=placevar,font=('맑은 고딕', 12))
weetak_lab = Label(post,text="* 위탁 시 위탁장소를 세부사항에 적어주세요.")

reward_lab.place(x=150,y=220)
reward_ent.place(x=250,y=220)
saryeh_lab.place(x=150,y=250)

# if(lost_btn)
# place = lost
# buffer = list(id,lost_btn)

write_btn = Button(post,text="작성",command= lambda: print(tagvar.get(),"\t",placevar.get()))
write_btn.place(x=150,y=320) 

test_lab = Label(post,text=str(tagvar.get())+"\t"+str(placevar.get()))
test_lab.place(x=150,y=280)

write_close_btn = Button(post,text="닫기",command=lambda: post.destroy())
write_close_btn.place(x=300,y=320) 

post.mainloop()
