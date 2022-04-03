from tkinter import *
from  tkinter.font import Font
import requests


root = Tk()
root.geometry("220x300")
root.configure(bg="black")
root.title("TicTacToe")
x=10
y=85



def api():
    s= ""
    for i in range(3):
        for j in range(3):
            s=s+board[i][j]
    s=s.strip()


    url="http://rahuliii.pythonanywhere.com/tictactoe.api.hg/{}".format(s).strip()


    res=requests.get(url)

    res=res.json()

    row=(res["move(row,column)"])[0]
    column=(res["move(row,column)"])[1]

    brain(row=int(row),column=int(column))
c=0
def check():
    global c
    if(board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X"):

        b00["state"]=DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re.configure(bg="white")
        re["state"]=NORMAL

        l1["text"]="you win"
    elif (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"):
        l1["text"] = "you win"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re.configure(bg="white")
        re["state"]=NORMAL

    elif (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"):
        l1["text"] = "you win"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re.configure(bg="white")
        re["state"] = NORMAL
    elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"):
        l1["text"] = "you win"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re.configure(bg="white")
        re["state"] = NORMAL
    elif (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"):
        l1["text"] = "you win"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re.configure(bg="white")
        re["state"] = NORMAL
    elif (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        l1["text"] = "you win"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")


    elif (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"):
        l1["text"] = "you win"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        l1["text"] = "you win"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O"):

        l1["text"] = "you lose"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O"):
        l1["text"] = "you lose"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
        l1["text"] = "you lose"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
        l1["text"] = "you lose"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O"):
        l1["text"] = "you lose"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        l1["text"] = "you lose"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
        l1["text"] = "you lose"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        l1["text"] = "you lose"

        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"] = NORMAL
        re.configure(bg="white")
    elif c==9:
        l1["text"]="Draw"
        b00["state"] = DISABLED
        b01["state"] = DISABLED
        b02["state"] = DISABLED
        b10["state"] = DISABLED
        b11["state"] = DISABLED
        b12["state"] = DISABLED
        b20["state"] = DISABLED
        b21["state"] = DISABLED
        b22["state"] = DISABLED
        re["state"]= NORMAL
        re.configure(bg="white")

board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

b=1
def brain(row,column):



    global b ,board,c



    if (row==0 and column==0):
        c=c+1
        if b==1:
            b00["text"]="X"
            b00["state"]=DISABLED

            board[0][0]= "X"
            check()
            b = 2

            api()


        elif(b==2):
            b00["text"]="O"
            b=1
            b00["state"]=DISABLED

            board[0][0] = "O"
            check()

    elif (row == 0 and column == 1):
        c = c + 1
        if b==1:
            b01["text"] = "X"
            b01["state"]=DISABLED
            b = 2
            a01 = "X"
            board[0][1] = "X"

            check()
            api()

        elif(b==2):
            b01["text"] = "O"
            b01["state"] = DISABLED
            b = 1
            board[0][1] = "O"

            check()

    elif (row == 0 and column == 2):
        c = c + 1
        if b==1:
            b02["text"] = "X"
            b02["state"]=DISABLED
            b = 2
            board[0][2] = "X"

            check()
            api()

        elif b==2:
            b02["text"] = "O"
            b02["state"]=DISABLED
            b = 1
            board[0][2] = "O"

            check()

    elif (row == 1 and column == 0):
        c = c + 1
        if b==1:
            b10["text"] = "X"
            b10["state"]=DISABLED

            b = 2
            board[1][0] = "X"

            check()
            api()

        elif b==2:
            b10["text"] = "O"
            b10["state"]=DISABLED
            b = 1
            board[1][0] = "O"

            check()

    elif (row == 1 and column == 1):
        c = c + 1
        if b==1:
            b11["text"] = "X"
            b11["state"] = DISABLED
            b = 2
            board[1][1] = "X"

            check()
            api()

        elif b==2:
            b11["text"] = "O"
            b11["state"] = DISABLED
            b = 1
            board[1][1] = "O"

            check()

    elif (row == 1 and column == 2):
        c = c + 1
        if b==1:
            b12["text"] = "X"
            b12["state"] = DISABLED
            b = 2
            board[1][2] = "X"

            check()
            api()

        elif b==2:
            b12["text"] = "O"
            b12["state"] = DISABLED
            b = 1
            board[1][2] = "O"

            check()

    elif (row == 2 and column == 0):
        c = c + 1
        if b==1:
            b20["text"] = "X"
            b20["state"] = DISABLED
            b = 2
            board[2][0] = "X"

            check()
            api()

        elif b==2:
            b20["text"] = "O"
            b20["state"] = DISABLED
            b = 1
            board[2][0] = "O"

            check()


    elif (row == 2 and column == 1):
        c = c + 1
        if b==1:
            b21["text"] = "X"
            b21["state"] = DISABLED
            b = 2
            board[2][1] = "X"
            check()
            api()

        elif b==2:
            b21["text"] = "O"
            b21["state"] = DISABLED
            b = 1
            board[2][1] = "O"
            check()

    elif (row == 2 and column == 2):
        c = c + 1
        if b==1:
            b22["text"] = "X"
            b22["state"] = DISABLED
            b = 2
            board[2][2] = "X"
            check()
            api()

        elif b==2:
            b22["text"] = "O"
            b22["state"] = DISABLED

            board[2][2] = "O"
            b = 1
            check()





def b_0_0():
    e=0
    f=0
    brain(row=e,column=f)


def b_0_1():
   e=0
   f=1
   brain(row=e,column=f)

def b_0_2():
    e = 0
    f = 2
    brain(row=e, column=f)

def b_1_0():
    e = 1
    f = 0
    brain(row=e, column=f)

def b_1_1():
    e = 1
    f = 1
    brain(row=e, column=f)

def b_1_2():
    e = 1
    f = 2
    brain(row=e, column=f)

def b_2_0():
    e = 2
    f = 0
    brain(row=e, column=f)

def b_2_1():
    e = 2
    f = 1
    brain(row=e, column=f)

def b_2_2():
    e = 2
    f = 2
    brain(row=e, column=f)
def re():
    global board,b,c
    b00["state"] = NORMAL
    b01["state"] = NORMAL
    b02["state"] = NORMAL
    b10["state"] = NORMAL
    b11["state"] = NORMAL
    b12["state"] = NORMAL
    b20["state"] = NORMAL
    b21["state"] = NORMAL
    b22["state"] = NORMAL
    re["state"] = DISABLED
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    b00["text"] = ""
    b01["text"] = ""
    b02["text"] = ""
    b10["text"] = ""
    b11["text"] = ""
    b12["text"] = ""
    b20["text"] = ""
    b21["text"] = ""
    b22["text"] = ""
    c=0
    b=1
    re.configure(bg="black")
    l1["text"]=""



f=Font(family="Helvetica",size=15)
f2=Font(family="Helvetica",size=12)
f3=Font(family="Helvetica",size=12)

ll = Label(root,width=15,height=2,text="H.Tic Tac Toe ",font=f,fg="white",bg="black")
ll.place(x=10,y=5)

l1=Label(root,width=10,height=2,font=f2,fg="white",bg="black")
l1.place(x=10,y=40)


b00=Button(root,width=6,height=3,command=b_0_0,font=f3,bg="white")
b00.place(x=x,y=y)



b01=Button(root,width=6,height=3,command=b_0_1,font=f3,bg="white")
b01.place(x=x+68,y=y)
b02=Button(root,width=6,height=3,command=b_0_2,font=f3,bg="white")
b02.place(x=x+135,y=y)
b10=Button(root,width=6,height=3,command=b_1_0,font=f3,bg="white")
b10.place(x=x,y=y+72)
b11=Button(root,width=6,height=3,command=b_1_1,font=f3,bg="white")

b11.place(x=x+68,y=y+72)
b12=Button(root,width=6,height=3,command=b_1_2,font=f3,bg="white")
b12.place(x=x+135,y=y+72)
b20=Button(root,width=6,height=3,command=b_2_0,font=f3,bg="white")
b20.place(x=x,y=y+143)
b21=Button(root,width=6,height=3,command=b_2_1,font=f3,bg="white")
b21.place(x=x+68,y=y+143)
b22=Button(root,width=6,height=3,command=b_2_2,font=f3,bg="white")
b22.place(x=x+135,y=y+143)


re =Button(root,width=4,height=1,text="Restart",command=re)
re.place(x=150,y=50)
re["state"]=DISABLED
re.configure(bg="black")













root.mainloop()
