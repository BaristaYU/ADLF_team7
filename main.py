from tkinter import * #GUI 모듈 import, 모든 함수 사용

userlist = list() #user db
board = list() #게시판 db
mailbox = list(list("") for i in range(10)) #메일함 개수 (인당 1개, 최대 10개)
logout_flag = False #메인 로그아웃용 flag (True면 logout)

boardnum = list("N/A" for i in range(10)) #글 번호 (행) (여유분 10개)
mainboard = list("N/A" for i in range(10)) #게시글 리스트(열) (여유분 10개) (없을 시 "N/A")
info_btn = list("N/A" for i in range(10)) #내용버튼 리스트(열) (여유분 10개) (없을 시 "N/A")
comp_btn = list("N/A" for i in range(10)) #완료버튼 리스트(열) (여유분 10개) (없을 시 "N/A")
mail_btn = list("N/A" for i in range(10)) #쪽지버튼 리스트(열) (여유분 10개) (없을 시 "N/A")
comp_chkr = list("N/A" for i in range(10)) #완료여부 리스트(열) (여유분 10개) (없을 시 "N/A")

tag = ['[찾습니다]','[주웠어요]'] #태그 목록
place = ['원위치','위탁','취득'] #장소 목록

userlist.append(['1234','1234','유용균',mailbox[0]]) #테스트용1
userlist.append(['5678','5678','김세상',mailbox[1]]) #테스트용2
userlist.append(['','','관리자',mailbox[2]]) #테스트용3
board.append(['',tag[0],'USB 혜화역 4시쯤','빨간 SANDISK','010-1234-1234','N/A']) #테스트문구1
board.append(['5678',tag[0],'정문 근처에서 키링을 잃어버렸어요 사례 있음','키링키링','N/A','만원']) #테스트문구2
board.append(['1234',tag[1],'비싸보이는 안경을 주웠어요','블루라이트인듯','010-1234-1234',place[0]]) #테스트문구3

announcement = "로그인 시에는 이름을 기재하지 않으셔도 됩니다." #실행 시 안내문구

def register(): #회원가입 함수.
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
        announcement = "이미 존재하는 ID입니다." #안내문구에 저장
    elif("" in (id,pw,name)): # 하나라도 값을 안채워놓으면
        announcement = "빈 칸을 모두 채워주세요." #안내문구에 저장
    else: #0, False: 없으면
        userlist.append([id,pw,name,mailbox[len(userlist)]]) #유저DB에 정보 저장
        # messagebox.showwarning("분실물 찾기 프로그램","회원가입 성공")
        announcement = "회원가입 성공" #안내문구에 저장

def userlogin():
    global announcement #안내문구 함수 밖까지 유지
    global logout_flag #로그아웃 깃발 함수 밖까지 유지

    id = id_ent.get() #id받기
    pw = pw_ent.get() #pw받기

    is_id = 0 #id 있는지 여부 초기값 0
    is_pw = 0 #pw 있는지 여부 초기값 0

    for i in userlist: #userlist에서 id,pw,name 리스트 받아올때:
        if i[0] == id and i[1] == pw: #만약 리스트의 id,pw가 입력값과 같으면
            is_id = 1 #맞게 입력했으므로 is_id에 1 전달
            is_pw = 1 #맞게 입력했으므로 is_pw에 1 전달
            name = i[2] #이름 가져오기
            break #가져왔으므로 for문 더 안돌게 break
        elif i[0] == id: #id,pw 모두는 다르되 만약 리스트의 id가 입력한 id와 같으면
            is_id = 1 #맞게 입력했으므로 is_id에 1 전달
            break #더 돌 필요 없으므로 break
        elif i[0] == pw: #pw만 맞는 경우
            is_pw = 1 #맞게 입력했으므로 is_pw에 1 전달
            break #더 돌 필요 없으므로 break

    if(is_id==0): #0, False: id가 일치하지 않으면 혹은 id,pw 둘다 틀리면(초기값 0에서 변화가 없으면)
        announcement = "아이디를 확인해 주십시오."
    elif(is_pw==0): #0, False: 비밀번호가 다르면
        announcement = "비밀번호가 다릅니다."
    else: #둘다 0이 아닌 경우 로그인 성공, 메인 돌입
        announcement = "로그인 성공"
        logout_flag = False #로그아웃용 깃발 False(새로 로그인할 때 대비 초기화)
        mainscreen(id,name) #메인화면 실행 - 유저 id, 이름 연계

def logout(name): #로그아웃 함수 (창 제목용 이름 받음)
    global logout_flag #로그아웃 깃발 함수 밖까지 쓰기 위해 global 선언
    warn = Toplevel(login) #login을 부모로 하는 창 warn 생성
    warn.title(name+"님의 이차원 보관소") #유저 이름 포함 제목
    warn.geometry('330x100') #해상도

    ask = Label(warn,text='로그아웃 하시겠습니까?',font=('맑은 고딕', 12)) #로그아웃 여부 묻는 라벨 생성
    ask.pack() #라벨 배치

    write_btn = Button(warn,text="확인",command=lambda:[flag(),warn.destroy()]) #확인버튼 누를 시 flag함수 실행 및 warn 창 종료
    write_btn.place(x=100,y=60)  #버튼 배치

    write_close_btn = Button(warn,text="취소",command=lambda: warn.destroy()) #취소버튼 누를 시 warn 창 종료
    write_close_btn.place(x=190,y=60)  #버튼 배치

def flag(): #로그아웃 깃발 세우는 함수
    global logout_flag #로그아웃 깃발 
    logout_flag=True

def close(): #프로그램 종료함수. 모든 창은 Login을 부모로 하는 Toplevel로 열려 있으므로 Login이 닫히면 모든 창이 닫힘.
    closing = Toplevel(login)
    closing.title("이차원 보관소")
    closing.geometry('250x100')

    ask = Label(closing,text='종료 하시겠습니까?',font=('맑은 고딕', 12))
    ask.pack()

    write_btn = Button(closing,text="확인",command=lambda:login.destroy())
    write_btn.place(x=70,y=60) 

    write_close_btn = Button(closing,text="취소",command=lambda: closing.destroy())
    write_close_btn.place(x=160,y=60) 

def mainscreen(id,name):
    global userlist
    init = True
    main = Toplevel(login)
    main.title(name+"님의 이차원 보관소")
    main.geometry('1366x768')

    def mainupdate():
        main.after(200,mainupdate)
        if logout_flag == True:
            main.destroy()

    welcome = Label(main,text=name+'님 환영합니다.',font=('맑은 고딕', 20))
    welcome.pack()

    initial(main,id,init)
        
    write_btn = Button(main,text="글쓰기",command = lambda: write(main,id))
    write_btn.place(x=400,y=650)

    mailbox_btn = Button(main,text="쪽지함",command = lambda: mailscreen(id))
    mailbox_btn.place(x=650,y=650)

    logout_btn = Button(main,text="로그아웃",command = lambda: logout(name))
    logout_btn.place(x=900,y=650)
    
    mainupdate()
    main.mainloop()

def initial(main,id,init):
    global userlist, boardnum, mainboard, info_btn, comp_btn, mail_btn
    pos_x,pos_y = 500,100

    if init != True: #첫 실행이 아니면: 기존에 있던거 초기화
        for i in range(len(boardnum)):
            if mainboard[i] != 'N/A':
                mainboard[i].place_forget()
            if info_btn[i] != 'N/A':
                info_btn[i].place_forget()
            if comp_btn[i] != 'N/A':
                comp_btn[i].place_forget()
            if mail_btn[i] != 'N/A':
                mail_btn[i].place_forget()

    #게시글 생성
    for index,i in enumerate(board):
        is_user = 0
        if i[0] == id:
            is_user = 1
        pos_x = 300
        if i[1] == '[찾습니다]' and i[-1] != 'N/A': #찾습니다 태그에, 사례가 N/A가 아닌 경우 (사례가 있는 경우)
            mainboard[index] = Label(main,text=i[1]+"\t"+i[2].replace("{","").replace("}",""),fg='red')
        else:
            mainboard[index] = Label(main,text=i[1]+"\t"+i[2].replace("{","").replace("}",""))
        mainboard[index].place(x=pos_x,y=pos_y)
        pos_x += 580
        info_btn[index] = Button(main,text="내용",command= lambda x= index:inform(x,id))
        info_btn[index].place(x=pos_x,y=pos_y)
        pos_x += 80
        if is_user == 1: #유저면 완료버튼, 아니면 쪽지버튼
            comp_btn[index] = Button(main,text="완료",command= lambda x=index: comp(x)) 
            #lambda가 없으면 python은 인터프리터이므로 void한 comp함수가 실행이 되버림.
            #그런데 boardnum에 있는 list는 아직 형성 전이므로,
            # lambda를 통해 comp함수를 '실행 하는 함수'를 전달하여 버튼 누를 시에만 접근할 수 있게 됨.
            comp_btn[index].place(x=pos_x,y=pos_y)
            mail_btn[index] = "N/A"
        else:
            mail_btn[index] = Button(main,text="쪽지",command=lambda x=index: sendmail(x,id))
            mail_btn[index].place(x=pos_x,y=pos_y)
            comp_btn[index] = "N/A"
        pos_y += 50 #개행

        boardnum[index] = [i[0], mainboard[index], info_btn[index], comp_btn[index], mail_btn[index]]
        
        if comp_chkr[index] != "N/A":
            comp(index)

def inform(x,id):
    #게시물 형식: id, 태그(0:찾 / 1:주), 제목, 세부사항, 전화번호(n/a), 사례(n/a) or 장소
    #information 형식: 태그, 세부사항, 전화번호(n/a), 사례(n/a) or 장소
    name = namechkr(id)
    info = Toplevel(login)
    info.title(name+"님의 이차원 보관소")
    info.geometry('500x400')
    
    information = board[x][3:]
    information.insert(0,board[x][1])

    details = Label(info,text="세부사항: "+"\t"+information[1])
    details.place(x=150,y=50)

    contact = Label(info, text="전화번호: "+"\t"+information[2])
    
    if information[2] == 'N/A':
        contact.config(text="전화번호:",state=DISABLED)
    
    contact.place(x=150,y=100)

    if information[0] == '[찾습니다]':
        reward = Label(info, text="사례: "+"\t"+information[3])
        if information[3] == 'N/A':
            reward.config(text="사례:",state=DISABLED)
        reward.place(x=150,y=150)
    else:
        reward = Label(info, text="장소: "+"\t"+information[3])
        reward.place(x=150,y=150)
    
    info_close_btn = Button(info,text="닫기",command=lambda: info.destroy())
    info_close_btn.place(x=225,y=350)

def comp(x):
    global boardnum,comp_chkr

    boardnum[x][1].config(fg='gray65')
    boardnum[x][2].config(state=DISABLED)
    if boardnum[x][3] != "N/A":
        boardnum[x][3].config(state=DISABLED)
    if boardnum[x][4] != "N/A": 
        boardnum[x][4].config(state=DISABLED)
    
    comp_chkr[x] = True
    
def sendmail(x,my_id):
    global userlist

    user_id = boardnum[x][0]

    def sending(user_id):
        global userlist
        for index,i in enumerate(userlist):
            if i[0] == user_id:
                userlist[index][3].insert(0,[namechkr(my_id),send_ent.get()])
                send_ent.delete(0,len(send_ent.get()))
                break
        
    send = Toplevel(login)
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
    name = namechkr(id)
    mbox = Toplevel(login)
    mbox.title(name+"님의 이차원 보관소")
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

def write(main,id):
    global board
    name = namechkr(id)
    post = Toplevel(login)
    post.title(name+"님의 이차원 보관소")
    post.geometry('500x400')

    def lost():
        place1_btn.place_forget()
        place2_btn.place_forget()
        place3_btn.place_forget()
        weetak_lab.place_forget()
        void_lab.place_forget()

        reward_lab.place(x=150,y=220)
        reward_ent.place(x=250,y=220)
        saryeh_lab.place(x=150,y=250)
        
    def find():
        reward_lab.place_forget()
        reward_ent.place_forget()
        saryeh_lab.place_forget()
        void_lab.place_forget()

        place1_btn.place(x=150,y=220)
        place2_btn.place(x=250,y=220)
        place3_btn.place(x=340,y=220)
        weetak_lab.place(x=150,y=250)
        place1_btn.select()

    tagvar = IntVar()
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

    placevar = IntVar()
    place1_btn = Radiobutton(post,text='원위치',value=0,variable=placevar,font=('맑은 고딕', 12))
    place2_btn = Radiobutton(post,text='위탁',value=1,variable=placevar,font=('맑은 고딕', 12))
    place3_btn = Radiobutton(post,text='취득',value=2,variable=placevar,font=('맑은 고딕', 12))
    weetak_lab = Label(post,text="* 위탁 시 위탁장소를 세부사항에 적어주세요.")

    reward_lab.place(x=150,y=220)
    reward_ent.place(x=250,y=220)
    saryeh_lab.place(x=150,y=250)

    def getdata(id,tagvar,placevar):
        global board,comp_chkr

        if tel_ent.get() == '':
            tel = 'N/A'
        else:
            tel = tel_ent.get()

        if tagvar == 0:
            if reward_ent.get() == '':
                last = 'N/A'
            else:
                last = reward_ent.get()
        else:
            last = place[placevar]

        if title_ent.get() != '' and info_ent.get() != '':
            board.insert(0,[id,tag[tagvar],title_ent.get(),info_ent.get(),tel,last])
            comp_chkr.insert(0,'N/A')
            initial(main,id,False)
            post.destroy()
        else:
            void_lab.place(x=150,y=280)

    write_btn = Button(post, text="작성", command=lambda: getdata(id,tagvar.get(), placevar.get()))
    write_btn.place(x=150,y=320) 

    write_close_btn = Button(post,text="닫기",command=lambda: post.destroy())
    write_close_btn.place(x=300,y=320) 

    void_lab = Label(post,text='필수사항을 전부 입력해주세요.')

    post.mainloop()

def namechkr(id):
    for i in userlist:
        if i[0] == id:
            return i[2]

login = Tk()
login.title("이차원 보관소")
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
regi_btn.place(x=225,y=300)

close_btn = Button(login,text="종료", command=close)
close_btn.place(x=350,y=300)

login.mainloop()