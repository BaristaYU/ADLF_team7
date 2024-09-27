from tkinter import *

userlist = list() #user db
board = list() #게시판 db
mailbox = list(list("") for i in range(10)) #메일함 개수 (인당 1개, 최대 10개)

boardnum = list("N/A" for i in range(10)) #글 번호 (행) (최대 10개)
mainboard = list(range(10)) #게시글 리스트(열) (최대 10개) (없으면 안되므로 "N/A" 없음)
info_btn = list(range(10)) #내용버튼 리스트(열) (최대 10개) (없으면 안되므로 "N/A" 없음)
comp_btn = list("N/A" for i in range(10)) #완료버튼 리스트(열) (최대 10개) (없을 시 "N/A")
mail_btn = list("N/A" for i in range(10)) #쪽지버튼 리스트(열) (최대 10개) (없을 시 "N/A")

tag = ['[찾습니다]','[주웠어요]']
place = ['원위치','위탁','취득']
status = [DISABLED,NORMAL]
userlist.append(['1234','1234','유용균',mailbox[0]]) #테스트용1
userlist.append(['5678','5678','김세상',mailbox[1]]) #테스트용2
userlist.append(['','','관리자',mailbox[2]]) #테스트용3
board.append(['',tag[0],'USB 혜화역 4시쯤','빨간 SANDISK','010-1234-1234',]) #테스트문구1
board.append(['5678',tag[0],'정문 근처에서 키링을 잃어버렸어요 사례 있음','키링키링','010-1234-1234','만원',True]) #테스트문구2
board.append(['1234',tag[1],'비싸보이는 안경을 주웠어요','블루라이트인듯','010-1234-1234',place[0]]) #테스트문구3

announcement = "로그인 시에는 이름을 기재하지 않으셔도 됩니다."

def register():
    global userlist #함수 밖까지 회원목록 유지
    global announcement #함수 밖까지 안내문구값 유지
    id = id_ent.get() #id받기
    pw = pw_ent.get() #pw받기
    name = name_ent.get() #name받기
    is_id = 0 # id중복여부, 초기값 0
    for i in userlist: #userlist에서 id,pw,name 리스트 받아올때:
        if i[0] == id: #만약 리스트의 id가 입력한 id와 같으면
            is_id = 1 #중복이 있는 것이므로 is_id에 1 전달 후 break
            break #없으면 0 유지
    if(is_id): #1, True: 있으면
        # messagebox.showwarning("분실물 찾기 프로그램","이미 존재하는 ID입니다.")
        announcement = "이미 존재하는 ID입니다."
    elif("" in (id,pw,name)): # 하나라도 값을 안채워놓으면
        announcement = "빈 칸을 모두 채워주세요." 
    else: #0, False: 없으면
        userlist.append([id,pw,name,mailbox[len(userlist)]])
        # messagebox.showwarning("분실물 찾기 프로그램","회원가입 성공")
        announcement = "회원가입 성공"

def userlogin():
    global userlist
    global announcement

    id = id_ent.get() #id받기
    pw = pw_ent.get() #pw받기

    is_id = 0 #id 있는지 여부 초기값 0
    is_pw = 0 #pw 있는지 여부 초기값 0

    for i in userlist: #userlist에서 id,pw,name 리스트 받아올때:
        if i[0] == id and i[1] == pw: #만약 리스트의 pw가 입력한 pw와 같으면
            is_id = 1
            is_pw = 1 #맞게 입력했으므로 is_pw에 1 전달
            name = i[2] #이름 가져오기
            break
        elif i[0] == id: #만약 리스트의 id가 입력한 id와 같으면
            is_id = 1 #맞게 입력했으므로 is_id에 1 전달
            break
        elif i[1] == pw:
            is_pw = 1
            break

    if(is_id==0): #0, False: id가 일치하지 않으면
        announcement = "아이디를 확인해 주십시오."
    elif(is_pw==0): #0, False: 비밀번호가 다르면
        announcement = "비밀번호가 다릅니다."
    else: #둘다 0이 아닌 경우 로그인 성공, 메인 돌입
        announcement = "로그인 성공"
        mainscreen(id,name)

def mainscreen(id,name):
    global userlist

    main = Tk()
    main.title('분실물 찾기 프로그램')
    main.geometry('1366x768')

    welcome = Label(main,text=name+'님 환영합니다.',font=('맑은 고딕', 20))
    welcome.pack()

    initial(main,id)
        
    write_btn = Button(main,text="글쓰기",command = write)
    write_btn.place(x=500,y=650)

    mailbox_btn = Button(main,text="쪽지함",command = lambda: mailscreen(id))
    mailbox_btn.place(x=800,y=650)

    main.mainloop()

def initial(main,id):
    global userlist, boardnum, mainboard, info_btn, comp_btn, mail_btn
    pos_x,pos_y = 500,100
    postnum = list()

    def comp(n):
        print(boardnum[n])
        boardnum[n][1].config(fg='gray65')
        boardnum[n][2].config(state=DISABLED)
        if boardnum[n][3] != "N/A":
            boardnum[n][3].config(state=DISABLED)
        if boardnum[n][4] != "N/A": 
            boardnum[n][4].config(state=DISABLED)

    #게시글 생성
    for index,i in enumerate(board):
        is_user = 0
        if i[0] == id:
            is_user = 1
        pos_x = 300
        if i[-1] == True:
            mainboard[index] = Label(main,text=i[1]+"\t"+i[2].replace("{","").replace("}",""),fg='red')
        else:
            mainboard[index] = Label(main,text=i[1]+"\t"+i[2].replace("{","").replace("}",""))
        mainboard[index].place(x=pos_x,y=pos_y)
        pos_x += 580
        info_btn[index] = Button(main,text="내용")
        info_btn[index].place(x=pos_x,y=pos_y)
        pos_x += 80
        if is_user == 1: #유저면 완료버튼, 아니면 쪽지버튼
            postnum.append(index)
            comp_btn[index] = Button(main,text="완료",command= lambda: comp(0)) 
            #lambda가 없으면 python은 인터프리터이므로 void한 comp함수가 실행이 되버림.
            #그런데 boardnum에 있는 list는 아직 형성 전이므로,
            # lambda를 통해 comp함수를 '실행 하는 함수'를 전달하여 버튼 누를 시에만 접근할 수 있게 됨.
            comp_btn[index].place(x=pos_x,y=pos_y)
        else:
            mail_btn[index] = Button(main,text="쪽지",command=lambda: sendmail(i[0],id))
            mail_btn[index].place(x=pos_x,y=pos_y)
        pos_y += 100 #개행
        boardnum[index] = [i[0], mainboard[index], info_btn[index], comp_btn[index], mail_btn[index]]

    for index, j in enumerate(boardnum):
        boardnum[j[3]]


def sendmail(user_id,my_id):
    global userlist
    def sending(user_id):
        global userlist
        for index,i in enumerate(userlist):
            if i[0] == user_id:
                userlist[index][3].insert(0,[namechkr(my_id),send_ent.get()])
                print(user_id)
                print(my_id)
                print(userlist[index])
                print(userlist[index][3])
                send_ent.delete(0,len(send_ent.get()))
                break
        
    send = Tk()
    send.title('쪽지 보내기')
    send.geometry('500x200')
    send_lab = Label(send, text='쪽지',font=('맑은 고딕', 10))
    send_lab.place(x=250,y=50)
    send_ent = Entry(send)
    send_ent.place(x=150,y=100)
    send_btn = Button(send,text="작성", command=lambda: sending(user_id))
    send_btn.place(x=150,y=150)
    send_close_btn = Button(send,text="닫기",command=lambda: send.destroy())
    send_close_btn.place(x=300,y=150)

    send.mainloop()

def mailscreen(id):
    global userlist

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
        global userlist

        mails = list() #쪽지함 불러오기
        pos = textbox.yview() #스크롤바 위치 저장
        textbox.delete("1.0",END) #쪽지함 초기화(후에 재생성)

        for index, i in enumerate(userlist):
            if i[0] == id:
                mails = userlist[index][3]
                break

        if len(mails) > 0:
            for j in mails:
                textbox.insert(END, j[0]+":"+"\t"+j[1]+"\n")

        textbox.yview(MOVETO,pos[0]) #스크롤바 저장된 위치로
        textbox.after(200,mailupdate) #0.2초마다 갱신

    mbox_close_btn = Button(mbox,text="닫기",command=lambda: mbox.destroy())
    mbox_close_btn.place(x=225,y=350)

    mailupdate()
    mbox.mainloop()

def notice():
    announce.config(text = announcement)
    announce.after(500,notice)

def write():
    post = Tk()
    post.title('글쓰기')
    post.geometry('500x400')
    placevar = IntVar()

    def lost():
        reward_lab = Label(post, text='사례 (선택)',font=('맑은 고딕', 10))
        reward_lab.place(x=150,y=220)
        reward_ent = Entry(post)
        reward_ent.place(x=250,y=220)
        saryeh_lab = Label(post,text="* 사례가 있을 시 글 제목이 강조됩니다.")
        saryeh_lab.place(x=150,y=250)

    def find():
        place1_btn = Radiobutton(post,text='원위치',value=1,variable=placevar,font=('맑은 고딕', 12))
        place1_btn.place(x=150,y=210)
        place1_btn.select()
        place2_btn = Radiobutton(post,text='위탁',value=2,variable=placevar,font=('맑은 고딕', 12))
        place2_btn.place(x=250,y=220)
        place3_btn = Radiobutton(post,text='취득',value=3,variable=placevar,font=('맑은 고딕', 12))
        place3_btn.place(x=350,y=220)
        weetak_lab = Label(post,text="* 위탁 시 위탁장소를 세부사항에 적어주세요.")
        weetak_lab.place(x=150,y=250)
        
    lost_btn = Radiobutton(post,text='찾습니다',value=1,command=lost)
    lost_btn.place(x=150,y=20)
    find_btn = Radiobutton(post,text='주웠어요',value=2,command=find)
    find_btn.place(x=250,y=20)

    lost_btn.select()

    title_lab = Label(post, text='제목 (필수)',font=('맑은 고딕', 10))
    title_lab.place(x=150,y=50)
    title_ent = Entry(post)
    title_ent.place(x=250,y=50)

    info_lab = Label(post, text='세부사항 (필수)',font=('맑은 고딕', 10))
    info_lab.place(x=150,y=100)
    info_ent = Entry(post)
    info_ent.place(x=250,y=100)

    tel_lab = Label(post, text='연락처 (필수)',font=('맑은 고딕', 10))
    tel_lab.place(x=150,y=170)
    tel_ent = Entry(post)
    tel_ent.place(x=250,y=170)

    write_btn = Button(post,text="작성")
    write_btn.place(x=225,y=320) 

    post.mainloop()

def namechkr(id):
    for i in userlist:
        if i[0] == id:
            return i[2]

login = Tk()
login.title('분실물 찾기 프로그램')
login.geometry('500x400')

name_lab = Label(login, text='이름',font=('맑은 고딕', 12))
name_lab.place(x=150,y=50)
name_ent = Entry(login)
name_ent.place(x=250,y=50)

id_lab = Label(login, text='학번',font=('맑은 고딕', 12))
id_lab.place(x=150,y=100)
id_ent = Entry(login)
id_ent.place(x=250,y=100)

pw_lab = Label(login, text='비밀번호',font=('맑은 고딕', 12))
pw_lab.place(x=150,y=150)
pw_ent = Entry(login)
pw_ent.place(x=250,y=150)

announce = Label(login, text=announcement)
announce.place(x=150, y=200)

notice()

login_btn = Button(login,text="로그인", command=userlogin)
login_btn.place(x=100,y=300)

regi_btn = Button(login,text="회원가입", command=register)
regi_btn.place(x=350,y=300)

login.mainloop()