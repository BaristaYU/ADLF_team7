from tkinter import * #GUI 모듈 import, 모든 함수 사용
import time #시간 표기 목적

userlist = list() #user db
board = list() #게시판 db
mailbox = list(list("") for i in range(10)) #메일함 개수 (인당 1개, 최대 10개)
logout_flag = False #메인 로그아웃용 flag (True면 logout)

tag = ['[찾습니다]','[주웠어요]'] #태그 목록
place = ['원위치','위탁','습득'] #장소 목록

boardnum = list("N/A" for i in range(10)) #글 번호 (행) (여유분 10개)
mainboard = list("N/A" for i in range(10)) #게시글 리스트(열) (여유분 10개) (없을 시 "N/A")
info_btn = list("N/A" for i in range(10)) #내용버튼 리스트(열) (여유분 10개) (없을 시 "N/A")
comp_btn = list("N/A" for i in range(10)) #완료버튼 리스트(열) (여유분 10개) (없을 시 "N/A")
mail_btn = list("N/A" for i in range(10)) #쪽지버튼 리스트(열) (여유분 10개) (없을 시 "N/A")
comp_chkr = list("N/A" for i in range(10)) #완료여부 리스트(열) (여유분 10개) (없을 시 "N/A")

userlist.append(['1234','1234','유용균',mailbox[0]]) #테스트용1
userlist.append(['5678','5678','김세상',mailbox[1]]) #테스트용2
userlist.append(['0000','0000','양초롱',mailbox[2]]) #테스트용4
userlist.append(['9999','9999','정예솔',mailbox[3]]) #테스트용5
userlist.append(['','','관리자',mailbox[4]]) #테스트용3

board.append(['0000',tag[0],'USB 혜화역 4시쯤','빨간 SANDISK','010-1234-1234','N/A','24/09/30 12:00']) #테스트문구1
board.append(['5678',tag[0],'정문 근처에서 키링을 잃어버렸어요 사례 있음','키링키링','N/A','만원','24/10/05 13:00']) #테스트문구2
board.append(['9999',tag[1],'비싸보이는 안경을 주웠어요','블루라이트인듯','010-1234-1234',place[0],'24/10/10 14:00']) #테스트문구3
board.append(['1234',tag[1],'길잃은 에어팟 한 쪽을 데리고 있습니다','왼쪽 에어팟이네요, 학과 사무실에 맡겨뒀어요.','010-1234-1234',place[1],'24/10/15 15:00']) #테스트문구4
board.append(['',tag[1],'관리자입니다.','관리자','0000',place[2],'24/10/20 16:00']) #테스트문구4

announcement = "모든 분실물이 모이는 곳, 이차원 보관소입니다." #실행 시 안내문구

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

    if is_id and id != "": #1, True: 있으면 / 관리자 아이디 숨기기
        announcement = "이미 존재하는 학번입니다." #안내문구에 저장
    elif "" in (id,pw,name): # 하나라도 값을 안채워놓으면
        announcement = "빈 칸을 모두 채워주세요." #안내문구에 저장
    elif len(name) == 1: #이름이 한글자면
        announcement = "이름은 최소 두 글자 이상이어야 합니다." #안내문구에 저장
    elif len(id) != len(id.strip()) or len(pw) != len(pw.strip()) or len(name) != len(name.strip()):
        announcement = "입력값에 공백이 없는지 확인해주세요." #안내문구에 저장
    else:
        try:
            int(id)
        except:
            announcement = "학번은 숫자만 사용 가능합니다." #안내문구에 저장
        else:
            userlist.append([id,pw,name,mailbox[len(userlist)-1]]) #유저DB에 정보 저장
            # messagebox.showwarning("분실물 찾기 프로그램","회원가입 성공")
            announcement = "회원가입 성공" #안내문구에 저장
            name_ent.delete(0,'end')
            id_ent.delete(0,'end')
            pw_ent.delete(0,'end')

def userlogin():
    global announcement #안내문구 함수 밖까지 유지
    global logout_flag #로그아웃 깃발 함수 밖까지 유지

    id = id_ent.get() #id받기
    pw = pw_ent.get() #pw받기

    name_ent.delete(0,'end')
    pw_ent.delete(0,'end')

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
        announcement = "학번을 확인해 주십시오."
    elif(is_pw==0): #0, False: 비밀번호가 다르면
        announcement = "비밀번호가 다릅니다."
    else: #둘다 0이 아닌 경우 로그인 성공, 메인 돌입
        announcement = "모든 분실물이 모이는 곳, 이차원 보관소입니다."
        id_ent.delete(0,'end')
        logout_flag = False #로그아웃용 깃발 False(새로 로그인할 때 대비 초기화)
        mainscreen(id,name) #메인화면 실행 - 유저 id, 이름 연계

def logout(name,main): #로그아웃 함수 (창 제목용 이름 받음)
    global logout_flag #로그아웃 깃발 함수 밖까지 쓰기 위해 global 선언
    warn = Toplevel(main) #main을 부모로 하는 창 warn 생성
    warn.title(name+"님의 이차원 보관소") #유저 이름 포함 제목
    warn.geometry('250x100+600+350') #해상도

    ask = Label(warn,text='로그아웃 하시겠습니까?',font=('나눔고딕', 12)) #로그아웃 여부 묻는 라벨 생성
    ask.pack(pady=20) #라벨 배치

    write_btn = Button(warn,text="확인",command=lambda:[flag(),warn.destroy()],font=('나눔고딕', 10)) #확인버튼 누를 시 flag함수 실행 및 warn 창 종료
    write_btn.place(x=60,y=60)  #버튼 배치

    write_close_btn = Button(warn,text="취소",command=lambda: warn.destroy(),font=('나눔고딕', 10)) #취소버튼 누를 시 warn 창 종료
    write_close_btn.place(x=150,y=60)  #버튼 배치

def flag(): #로그아웃 깃발 세우는 함수
    global logout_flag #로그아웃 깃발 
    logout_flag=True

def close(name): #프로그램 종료함수. 모든 창은 Login을 부모로 하는 Toplevel로 열려 있으므로 Login이 닫히면 모든 창이 닫힘.
    closing = Toplevel(login)

    if name != '':
        closing.title(name+"님의 이차원 보관소")
    else:
        closing.title("이차원 보관소")

    closing.geometry('250x100+620+350')

    ask = Label(closing,text='종료 하시겠습니까?',font=('나눔고딕', 12))
    ask.pack(pady=20)

    write_btn = Button(closing,text="확인",command=lambda:login.destroy(),font=('나눔고딕', 10))
    write_btn.place(x=60,y=60) 

    write_close_btn = Button(closing,text="취소",command=lambda: closing.destroy(),font=('나눔고딕', 10))
    write_close_btn.place(x=150,y=60) 

def mainscreen(id,name):
    global userlist, all_rad
    init = True
    bg = 'space_shade.png'
    main = Toplevel(login)
    main.title(name+"님의 이차원 보관소")
    main.geometry('1366x768+70+50')
    img = PhotoImage(file=bg)

    def mainupdate():
        main.after(200,mainupdate)
        if logout_flag == True:
            main.destroy()
    
    def selector(postvar,id):
        global boardnum
        my_board = list()
        lt_board = list()
        fd_board = list()

        pos_y = 170

        for i in range(len(boardnum)):
            if mainboard[i] != 'N/A':
                mainboard[i].place_forget()
            if info_btn[i] != 'N/A':
                info_btn[i].place_forget()
            if comp_btn[i] != 'N/A':
                comp_btn[i].place_forget()
            if mail_btn[i] != 'N/A':
                mail_btn[i].place_forget()

        if postvar == 0:
            initial(main,id,False)

        if postvar == 1:
            pos_x = 130

            for lt in boardnum:
                if lt[-1] == '[찾습니다]' and lt != 'N/A':
                    lt_board.append(lt)
            for lt2 in lt_board:
                pos_x = 130
                lt2[1].place(x=pos_x,y=pos_y) #제목
                pos_x += 930 #780
                lt2[2].place(x=pos_x,y=pos_y) #내용
                pos_x += 80
                if lt2[3] != 'N/A': #완료버튼 n/a 아니면
                    lt2[3].place(x=pos_x,y=pos_y) #완료
                else: #아니면 쪽지
                    lt2[4].place(x=pos_x,y=pos_y)
                pos_y += 50 #개행

        if postvar == 2:
            pos_x = 130

            for fd in boardnum:
                if fd[-1] == '[주웠어요]' and fd != 'N/A':
                    fd_board.append(fd)
            for fd2 in fd_board:
                pos_x = 130
                fd2[1].place(x=pos_x,y=pos_y) #제목
                pos_x += 930 #780
                fd2[2].place(x=pos_x,y=pos_y) #내용
                pos_x += 80
                if fd2[3] != 'N/A': #완료버튼 n/a 아니면
                    fd2[3].place(x=pos_x,y=pos_y) #완료
                else: #아니면 쪽지
                    fd2[4].place(x=pos_x,y=pos_y)
                pos_y += 50 #개행

        if postvar == 3:
            pos_x = 130

            for my in boardnum:
                if my[0] == id and my != 'N/A':
                    my_board.append(my)
            for my2 in my_board:
                pos_x = 130
                my2[1].place(x=pos_x,y=pos_y) #제목
                pos_x += 930 #780
                my2[2].place(x=pos_x,y=pos_y) #내용
                pos_x += 80
                if my2[3] != 'N/A': #완료버튼 n/a 아니면
                    my2[3].place(x=pos_x,y=pos_y) #완료
                else: #아니면 쪽지
                    my2[4].place(x=pos_x,y=pos_y)
                pos_y += 50 #개행

    bg_img = Label(main,image=img)
    bg_img.pack()

    welcome = Label(main,text=name+'님 환영합니다.',font=('나눔고딕', 20),fg='white',background='#0B0911')
    welcome.place(x=570,y=20)

    postvar = IntVar()
    all_rad = Radiobutton(main,text='전체 글',value=0,variable=postvar,command=lambda:selector(postvar.get(),id),font=('나눔고딕', 12),fg='white',background='#0B0911',selectcolor='#0B0911',activebackground='#0B0911',activeforeground='white')
    all_rad.place(x=130,y=80) 
    find_rad = Radiobutton(main,text='[찾습니다]',value=1,variable=postvar,command=lambda:selector(postvar.get(),id),font=('나눔고딕', 12),fg='white',background='#0B0911',selectcolor='#0B0911',activebackground='#0B0911',activeforeground='white')
    find_rad.place(x=270,y=80)
    find_rad = Radiobutton(main,text='[주웠어요]',value=2,variable=postvar,command=lambda:selector(postvar.get(),id),font=('나눔고딕', 12),fg='white',background='#0B0911',selectcolor='#0B0911',activebackground='#0B0911',activeforeground='white')
    find_rad.place(x=420,y=80)  
    find_rad = Radiobutton(main,text='내가 쓴 글',value=3,variable=postvar,command=lambda:selector(postvar.get(),id),font=('나눔고딕', 12),fg='white',background='#0B0911',selectcolor='#0B0911',activebackground='#0B0911',activeforeground='white')
    find_rad.place(x=580,y=80)  

    menu_1 = Label(main,text="글번호",font=('나눔고딕', 14),fg='white',background='#0B0911')
    menu_1.place(x=130,y=120) #230
    menu_2 = Label(main,text="이름",font=('나눔고딕', 14),fg='white',background='#0B0911')
    menu_2.place(x=228,y=120) #328
    menu_3 = Label(main,text="게시판",font=('나눔고딕', 14),fg='white',background='#0B0911')
    menu_3.place(x=324,y=120) #424
    menu_4 = Label(main,text="제목",font=('나눔고딕', 14),fg='white',background='#0B0911')
    menu_4.place(x=444,y=120) #544

    initial(main,id,init)
    
    qmark = 'qmark.png'
    tutimg = PhotoImage(file=qmark)
    tutbtn = Button(main, image=tutimg, command = lambda: tutorial(name,main),highlightthickness = 0, bd=0, activebackground='#0F101F')
    tutbtn.place(x=160,y=648)

    write_btn = Button(main,text="글쓰기",command = lambda: write(main,id),font=("나눔고딕", 12))
    write_btn.place(x=350,y=650,width=85,height=38)

    mailbox_btn = Button(main,text="쪽지함",command = lambda: mailscreen(id,main),font=("나눔고딕", 12))
    mailbox_btn.place(x=590,y=650,width=85,height=38)

    logout_btn = Button(main,text="로그아웃",command = lambda: logout(name,main),font=("나눔고딕", 12))
    logout_btn.place(x=830,y=650,width=85,height=38)

    exit_btn = Button(main,text="종료",command = lambda: close(name),font=("나눔고딕", 12))
    exit_btn.place(x=1070,y=650,width=85,height=38)
    
    mainupdate()
    main.mainloop()

def tutorial(name,main):
    tuto = Toplevel(main)
    tuto.title(name+"님의 이차원 보관소")
    tuto.geometry('1366x768+70+50') #270+140

    main.withdraw()

    tuto_bg_path = 'tutorial_1366_768.png'
    tuto_bg = PhotoImage(file = tuto_bg_path)
    tuto_screen = Label(tuto, image=tuto_bg)
    tuto_screen.pack()
    
    tuto_exit_btn = Button(tuto,text='튜토리얼 끝내기',command=lambda:[tuto.destroy(),main.deiconify()],font=("나눔고딕", 20))
    tuto_exit_btn.place(x=1050,y=50,width=250,height=58)

    tuto.mainloop()

def initial(main,id,init):
    global boardnum, mainboard, info_btn, comp_btn, mail_btn, all_rad
    pos_y = 170

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
        pos_x = 130 #230
        if i[1] == '[찾습니다]' and i[-2] != 'N/A': #찾습니다 태그에, 사례가 'N/A'가 아닌 경우 (사례가 있는 경우)
            buffer = list(namechkr(i[0]))
            if len(buffer) == 2:
                buffer[-1] = '*'
            else:
                for j in range(1,len(buffer)-1):
                    buffer[j] = '*'
            name = "".join(buffer)
            mainboard[index] = Label(main,text=str(index+1)+"\t"+name+"\t"+i[1]+"\t     "+i[2],fg='tomato',background='#0B0911',font=("나눔고딕", 14))
        else:
            buffer = list(namechkr(i[0]))
            if len(buffer) == 2:
                buffer[-1] = '*'
            else:
                for j in range(1,len(buffer)-1):
                    buffer[j] = '*'
            name = "".join(buffer)
            mainboard[index] = Label(main,text=str(index+1)+"\t"+name+"\t"+i[1]+"\t     "+i[2],fg='white',background='#0B0911',font=("나눔고딕", 14))
        mainboard[index].place(x=pos_x,y=pos_y)
        pos_x += 930 #780
        info_btn[index] = Button(main,text="내용",command= lambda x= index:inform(x,id,main),font=("나눔고딕", 12))
        info_btn[index].place(x=pos_x,y=pos_y)
        pos_x += 80
        if is_user == 1: #유저면 완료버튼, 아니면 쪽지버튼
            comp_btn[index] = Button(main,text="완료",command= lambda x=index: comp(x),font=("나눔고딕", 12)) 
            #lambda가 없으면 python은 인터프리터이므로 void한 comp함수가 실행이 되버림.
            #그런데 boardnum에 있는 list는 아직 형성 전이므로,
            # lambda를 통해 comp함수를 '실행 하는 함수'를 전달하여 버튼 누를 시에만 접근할 수 있게 됨.
            comp_btn[index].place(x=pos_x,y=pos_y)
            mail_btn[index] = "N/A"
        else:
            mail_btn[index] = Button(main,text="쪽지",command=lambda x=index: sendmail(x,id,main),font=("나눔고딕", 12))
            mail_btn[index].place(x=pos_x,y=pos_y)
            comp_btn[index] = "N/A" #재접속시 toplevel.!button4는 destroy되는데,
                                    #2번째 버튼에 저장된 toplevel.!button4에 config명령을 줘버려서 에러터짐
        pos_y += 50 #개행

        boardnum[index] = [i[0], mainboard[index], info_btn[index], comp_btn[index], mail_btn[index], i[1]]
        
        if comp_chkr[index] != "N/A":
            complete(index)

        all_rad.select()

def inform(x,id,main):
    #게시물 형식: id, 태그(0:찾 / 1:주), 제목, 세부사항, 전화번호(n/a), 사례(n/a) or 장소
    #information 형식: 태그, 세부사항, 전화번호(n/a), 사례(n/a) or 장소
    name = namechkr(id)
    info = Toplevel(main)
    info.title(name+"님의 이차원 보관소")
    info.geometry('400x360+550+280')
    
    information = board[x][3:]
    information.insert(0,board[x][1])

    details = Label(info,text="세부사항: ",font=('나눔고딕',12))
    details.place(x=50,y=30)

    f1 = Frame(info)
    f1.place(x=133,y=32) #52
    details_txt = Text(f1, width=20, height=5, font=("나눔고딕", 12))
    sbar1 = Scrollbar(f1, orient="vertical",command=details_txt.yview)
    details_txt.insert(END, information[1])
    details_txt.pack(side="left", fill="y")
    sbar1.pack(side="right", fill="y")
    details_txt.config(state=DISABLED,bd=1,bg='SystemButtonFace',yscrollcommand=sbar1.set)
    
    contact = Label(info, text="연락처:",font=('나눔고딕',12))
    contact.place(x=50,y=140)
    contact.config(state=DISABLED)

    f2 = Frame(info)
    f2.place(x=133,y=142)
    contact_txt = Text(f2, width=20, height=2, font=("나눔고딕", 12))
    sbar2 = Scrollbar(f2, orient="vertical",command=contact_txt.yview)
    contact_txt.config(bd=1,bg='SystemButtonFace',yscrollcommand=sbar2.set)

    contact_txt.pack(side="left", fill="y")
    sbar2.pack(side="right", fill="y")
    
    if information[2] != 'N/A':
        contact.config(state=NORMAL)
        contact_txt.insert(END, information[2])
        contact_txt.config(state=DISABLED)

    saryeh = Label(info, text="사례:",font=('나눔고딕',12))

    f3 = Frame(info)
    saryeh_txt = Text(f3, width=20, height=2, font=('나눔고딕',12))
    sbar3 = Scrollbar(f3, orient="vertical",command=saryeh_txt.yview)
    saryeh_txt.config(bd=1,bg='SystemButtonFace',yscrollcommand=sbar3.set)

    saryeh_txt.pack(side="left", fill="y")
    sbar3.pack(side="right", fill="y")
 
    if information[0] == '[찾습니다]':
        saryeh.place(x=50,y=203)
        f3.place(x=133,y=205)
        if information[3] == 'N/A':
            saryeh.config(state=DISABLED)
        else:
            saryeh_txt.insert(END,information[3])
            saryeh_txt.config(state=DISABLED)
            
    else:
        wichi = Label(info, text="장소: "+"\t"+information[3],font=('나눔고딕',12))
        wichi.place(x=50,y=221)
    
    date = Label(info, text="작성일: "+"\t"+information[4],font=('나눔고딕',12))
    date.place(x=50,y=265)

    info_close_btn = Button(info,text="닫기",command=lambda: info.destroy(),font=('나눔고딕',12))
    info_close_btn.place(x=185,y=310)

def comp(x):
    check = Toplevel(login)
    check.title(namechkr(board[x][0])+"님의 이차원 보관소") 
    check.geometry('250x100+620+350') #해상도

    check_ask = Label(check,text='완료 하시겠습니까?',font=('나눔고딕', 12))
    check_ask.pack(pady=20) #라벨 배치

    yes_btn = Button(check,text="확인",command=lambda:[complete(x),check.destroy()],font=('나눔고딕', 10))
    yes_btn.place(x=60,y=60)  #버튼 배치

    no_btn = Button(check,text="취소",command=lambda: check.destroy(),font=('나눔고딕', 10)) #취소버튼 누를 시 warn 창 종료
    no_btn.place(x=150,y=60)  #버튼 배치

def complete(x):
    global boardnum,comp_chkr

    buffer = list(namechkr(board[x][0]))
    buffer[1] = '*'
    name = "".join(buffer)

    boardnum[x][1].config(text=str(x+1)+"\t"+name+"\t"+board[x][1]+"\t     "+"[완료된 글입니다.]",fg='gray65')
    boardnum[x][2].config(state=DISABLED)
    if boardnum[x][3] != "N/A":
        boardnum[x][3].config(state=DISABLED)
    if boardnum[x][4] != "N/A": 
        boardnum[x][4].config(state=DISABLED)
    
    comp_chkr[x] = True   
    
def sendmail(x,my_id,main):
    global userlist
    name = namechkr(my_id)
    user_id = boardnum[x][0]
    buffer = list(namechkr(user_id))
    if len(buffer) == 2:
        buffer[-1] = '*'
    else:
        for j in range(1,len(buffer)-1):
            buffer[j] = '*'
    user_name = "".join(buffer)

    def sending(user_id):
        global userlist

        if send_ent.get('1.0', END) != '\n' and len(send_ent.get('1.0', END)) <= 61:
            for index,i in enumerate(userlist):
                if i[0] == user_id:
                    userlist[index][3].insert(0,[namechkr(my_id),send_ent.get('1.0', END),' ['+time.strftime('%Y')[2:]+time.strftime('/%m/%d %H:%M]\n')])
                    send_ent.delete('1.0',END)
                    break
            note.place_forget()
        else:
            if send_ent.get('1.0', END) == '\n':
                note.place_forget()
                note.config(text='공란은 전송할 수 없습니다.')
                note.place(x=50,y=145)

            if len(send_ent.get('1.0', END)) >= 61: #get 끝에 '\n'이 붙기 때문에, 61자 초과 시
                note.place_forget()
                note.config(text='글자수 제한을 벗어났습니다. 현재 글자수: '+str(len(send_ent.get('1.0', END)))+'/60')
                note.place(x=50,y=145)
        
    send = Toplevel(main)
    send.title(name+"님의 이차원 보관소")
    send.geometry('400x230+550+280')
    send_lab = Label(send, text=user_name+'님께 쪽지 보내기',font=('나눔고딕', 12))
    send_lab.pack(pady=10)
    send_ent = Text(send,font=('나눔고딕', 12))
    send_ent.place(x=50,y=50,width=300,height=90)

    note = Label(send,font=('나눔고딕', 10))
    note.place()

    send_btn = Button(send,text="작성", command=lambda: sending(user_id),font=('나눔고딕', 11))
    send_btn.place(x=100,y=180)
    send_close_btn = Button(send,text="닫기",command=lambda: send.destroy(),font=('나눔고딕', 11))
    send_close_btn.place(x=250,y=180)

    send.mainloop()

def mailscreen(id,main):
    global userlist
    name = namechkr(id)
    mbox = Toplevel(main)
    mbox.title(name+"님의 이차원 보관소")
    mbox.geometry('500x430+500+230')

    frame = Frame(mbox)
    frame.pack()

    mboxlabel = Label(frame,text="쪽지함",font=('나눔고딕', 12))
    mboxlabel.pack(pady=10)

    textbox = Text(frame, width=38, height=17, font=("나눔고딕", 12))
    scrollbar = Scrollbar(frame, orient="vertical",command=textbox.yview)
    textbox.configure(yscrollcommand=scrollbar.set)
    
    textbox.pack(side="left",fill="y")
    scrollbar.pack(side="right", fill="y")

    def mailupdate():
        mails = list() #쪽지함 불러오기
        textbox.config(state=NORMAL)
        pos = textbox.yview() #스크롤바 위치 저장
        textbox.delete('1.0',END) #쪽지함 초기화(후에 재생성)
        
        for index, i in enumerate(userlist):
            if i[0] == id:
                mails = userlist[index][3]
                break
        
        if len(mails) > 0:
            for j in mails:
                textbox.insert(END, j[0]+j[2]+':   '+j[1])
                
        textbox.yview(MOVETO,pos[0]) #스크롤바 저장된 위치로
        textbox.config(state=DISABLED)
        textbox.after(200,mailupdate) #0.2초마다 갱신

    mbox_close_btn = Button(mbox,text="닫기",command=lambda: mbox.destroy(),font=('나눔고딕',11))
    mbox_close_btn.place(x=225,y=385)

    mailupdate()
    mbox.mainloop()

def notice():
    announce.config(text = announcement)
    announce.after(200,notice)

def write(main,id):
    global board
    name = namechkr(id)
    post = Toplevel(main)
    post.title(name+"님의 이차원 보관소")
    post.geometry('573x400+440+200') #500 - 800

    def lost():
        place1_btn.place_forget()
        place2_btn.place_forget()
        place3_btn.place_forget()
        weetak_lab.place_forget()

        reward_place_lab.config(text='사례')
        optional_2.place(x=87, y=250)
        reward_ent.place(x=150,y=252,width=405)
        saryeh_lab.place(x=20,y=280)
        
    def find():
        reward_ent.place_forget()
        optional_2.place_forget()
        saryeh_lab.place_forget()

        reward_place_lab.config(text='장소')
        place1_btn.place(x=146,y=247) #237
        place2_btn.place(x=246,y=247)
        place3_btn.place(x=336,y=247)
        weetak_lab.place(x=20,y=280)
        place1_btn.select()

    tagvar = IntVar()
    lost_btn = Radiobutton(post,text='찾습니다',value=0,variable=tagvar,command=lost,font=('나눔고딕', 12))
    lost_btn.place(x=146,y=53) 
    find_btn = Radiobutton(post,text='주웠어요',value=1,variable=tagvar,command=find,font=('나눔고딕', 12))
    find_btn.place(x=250,y=53)  

    lost_btn.select()

    title_lab = Label(post, text='제목',font=('나눔고딕', 12))
    title_lab.place(x=20,y=20)
    mandatory_1 = Label(post, text='(필수)',font=('나눔고딕', 12), fg='red')
    mandatory_1.place(x=87, y=20)

    title_ent = Entry(post,font=('나눔고딕', 12))
    title_ent.place(x=150,y=22,width=405) #220

    info_lab = Label(post, text='세부사항',font=('나눔고딕', 12))
    info_lab.place(x=20,y=55)
    mandatory_2 = Label(post, text='(필수)',font=('나눔고딕', 12), fg='red')
    mandatory_2.place(x=87, y=55)

    info_ent = Text(post,font=('나눔고딕', 12),width=53, height=6)
    info_ent.place(x=20,y=90)

    tel_lab = Label(post, text='연락처',font=('나눔고딕', 12))
    tel_lab.place(x=20,y=215)
    optional_1 = Label(post, text='(선택)',font=('나눔고딕', 12))
    optional_1.place(x=87, y=215)

    tel_ent = Entry(post,font=('나눔고딕', 12))
    tel_ent.place(x=150,y=217,width=405)

    reward_place_lab = Label(post, text='사례',font=('나눔고딕', 12))
    optional_2 = Label(post, text='(선택)',font=('나눔고딕', 12))

    reward_ent = Entry(post,font=('나눔고딕', 12))
    saryeh_lab = Label(post,text="* 사례가 있을 시 글 제목이 강조됩니다.",font=('나눔고딕', 10))

    placevar = IntVar()
    place1_btn = Radiobutton(post,text='원위치',value=0,variable=placevar,font=('나눔고딕', 12))
    place2_btn = Radiobutton(post,text='위탁',value=1,variable=placevar,font=('나눔고딕', 12))
    place3_btn = Radiobutton(post,text='습득',value=2,variable=placevar,font=('나눔고딕', 12))
    weetak_lab = Label(post,text="* 위탁 시 위탁장소를 세부사항에 적어주세요.",font=('나눔고딕', 10))

    reward_place_lab.place(x=20,y=250)
    optional_2.place(x=87, y=250)
    reward_ent.place(x=150,y=252,width=405)
    saryeh_lab.place(x=20,y=280)

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

        title_len = len(title_ent.get())
        title_max30.config(text='글자수 제한을 벗어났습니다. 현재 글자수: '+str(title_len)+'/30')

        if 0 < title_len <= 30 and info_ent.get('1.0', END) != '\n':
            board.insert(0,[id,tag[tagvar],title_ent.get(),info_ent.get('1.0', END),tel,last,time.strftime('%Y')[2:]+time.strftime('/%m/%d %H:%M')])
            comp_chkr.insert(0,'N/A')
            initial(main,id,False)
            post.destroy()

        elif title_len > 30: #제목 글자수 초과 시
            title_max30.place(x=150,y=3)
            if info_ent.get('1.0', END) == '\n':
                void_lab.place(x=190,y=305)

        else:
            void_lab.place(x=190,y=305)
            if title_len <= 30:
                title_max30.place_forget()

    write_btn = Button(post, text="작성", command=lambda: getdata(id,tagvar.get(), placevar.get()),font=('나눔고딕', 12))
    write_btn.place(x=170,y=340) 

    write_close_btn = Button(post,text="닫기",command=lambda: post.destroy(),font=('나눔고딕', 12))
    write_close_btn.place(x=370,y=340) 

    void_lab = Label(post,text='필수사항을 전부 입력해주세요.',font=('나눔고딕', 12))
    title_max30 = Label(post,font=('나눔고딕', 8))

    post.mainloop()

def namechkr(id):
    for i in userlist:
        if i[0] == id:
            return i[2]

login = Tk()
login.title("이차원 보관소")
login.geometry('480x400+500+200')

name_lab = Label(login, text='이름',font=('나눔고딕', 12))
name_lab.place(x=100,y=48)
name_ent = Entry(login,font=('나눔고딕', 12))
name_ent.place(x=180,y=50)

id_lab = Label(login, text='학번',font=('나눔고딕', 12))
id_lab.place(x=100,y=98)
id_ent = Entry(login,font=('나눔고딕', 12))
id_ent.place(x=180,y=100)

pw_lab = Label(login, text='비밀번호',font=('나눔고딕', 12))
pw_lab.place(x=100,y=148)
pw_ent = Entry(login,font=('나눔고딕', 12),show="*")
pw_ent.place(x=180,y=150)

announce = Label(login, text=announcement,font=('나눔고딕', 12))
announce.place(x=90, y=200)
join = Label(login, text="회원가입 시 이름, 학번, 비밀번호를 기재하셔야 합니다.",font=('나눔고딕', 10))
join.place(x=90, y=240)
loginannounce = Label(login,text="로그인 시에는 이름을 기재하지 않으셔도 됩니다.",font=('나눔고딕', 10))
loginannounce.place(x=90, y=260)


notice()

login_btn = Button(login,text="로그인", command=userlogin,font=('나눔고딕', 10))
login_btn.place(x=80,y=300,width=70 , height=30)

regi_btn = Button(login,text="회원가입", command=register,font=('나눔고딕', 10))
regi_btn.place(x=205,y=300,width=70 , height=30)

close_btn = Button(login,text="종료", command=lambda:close(''),font=('나눔고딕', 10))
close_btn.place(x=330,y=300,width=70 , height=30)

login.mainloop()