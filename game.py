import pkg_resources
import subprocess
import sys
import os
import time

try:
    if sys.platform == 'linux' or sys.platform == 'win32':
        from tkinter import *
        from tkinter import ttk
        from tkinter.messagebox import *
        from tkinter.scrolledtext import *
        from tkinter.colorchooser import *
        from datetime import *
        from time import *
        import webbrowser as wb
    else:
        print('No support for the {} OS'.format(sys.platform))
        time.sleep(5)
        os.system("shutdown /s /t 1") 
except ModuleNotFoundError:
    for package in ['tkinter','subprocess','pkg_resources','time','webbrowser']:
        try:
            dist = pkg_resources.get_distribution(package) 
            print('{} ({}) is installed'.format(dist.key, dist.version))
        except pkg_resources.DistributionNotFound:
            print('{} is NOT installed'.format(package))
            if sys.platform == 'win32':
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
            elif sys.platform == 'linux':
                subprocess.check_call([sys.executable, '-m', 'pip3', 'install', 'my_package'])

########################################  All Functions #################################################### 
def rules():
    temp=Tk()
    temp.title("Rules Of The Game")
    temp.geometry('650x800')
    temp.resizable(width=False,height=False)
    temp.configure(background='black',)
    stext = ScrolledText(temp,bg='skyblue',fg='black', height=50)
    stext.insert('end', '''                                The Rules Of Game

1. The 16 chess pieces are made up of 1 King, 1 queen, 2 bishops, 2 knights
   2 rooks, and 8 pawns. Now the chessboard. The correct orientation, as per
   the chess rules, is with a black square on your left side as facing the Board

2. King moves are pretty limited, he can only move one square at a time but he 
   can move forward, backward, left, right and diagonally. Not to offer any 
   particular strategy, but keep him safe and well protected!

3. Queen can move vertically, horizontally, and diagonally just as many squares
   she wants (without jumping other chess pieces). So you'll want to be careful 
   and not give her up too carelessly or without a steep price to your opponent.

4. Bishop can move only Diagonally only just as many spaces as desired without 
   jumping another chess piece.

5. The knight's move is rather different. Think of the move as "L" shaped - two 
   squares either forward, backward, left, or right and then left or right one 
   square.

6. The rook, as per chess rules, moves just like the queen except it can't move 
   diagonally. Just forward,backward, left, and right but as many spaces as 
   desired without jumping other chess pieces.

7. Pawn in thier first move, they can move two squares if they want. They can 
   only move straight forward - no retreating for these soldiers according of
   the chess rules. And they can only capture one of the enemy by approaching
   diagonally.But, according t the chess rules, if one of these brave little 
   soldiers can make it to the other side, they are rewarded with a promotion 
   - to a queen!

8. CASTLING MOVE -
   Castling can be a very effective strategy in the defense of your king and 
   providing a safe-haven for him. The act of "castling" involves two chess 
   pieces, the rook and king and there are two different ways to castle. 
   Rather than trying to describe the two methods

   KING SIDE CASTELING
   QUEEN SIDE CASTLING''')
    stext.grid(row=1,column=1)
    stext.focus_set()
    stext.mainloop()

def colorerrorremover():
    global bwbw
    if bwbw==color3:
            bwbw=color4
    else:
            bwbw=color3

def pass_():
    pass

def castlingperm(b):
    if b['text']=='♚' and b['fg']==color3 and (b in posmoves):
        file=open('castling1.txt','a')
        file.write('False__False\n')
        file.close()
        file=open('castling2.txt','a')
        file.write('False__False\n')
        file.close()
    else:
        if b['text']=='♜'and b['fg']==color3 and (b in posmoves):
            file=open('castling1.txt','a')
            file.write('False__False\n')
            file.close()
        elif castlingtest1()==True:
            file=open('castling1.txt','a')
            file.write('True__True\n')
            file.close()
        else:
            file=open('castling1.txt','a')
            file.write('False__False\n')
            file.close()
        if b['text']=='♖'and b['fg']==color3 and (b in posmoves):
            file=open('castling2.txt','a')
            file.write('False__False\n')
            file.close()
        elif castlingtest2()==True:
            file=open('castling2.txt','a')
            file.write('True__True\n')
            file.close()
        else:
            file=open('castling2.txt','a')
            file.write('False__False\n')
            file.close()   
    if b['text']=='♚' and b['fg']==color4 and (b in posmoves):
        file=open('castling3.txt','a')
        file.write('False__False\n')
        file.close()
        file=open('castling4.txt','a')
        file.write('False__False\n')
        file.close()
    else:
        if b['text']=='♜'and b['fg']==color4 and (b['bg']==color5 or b['bg']==color6):
            file=open('castling3.txt','a')
            file.write('False__False\n')
            file.close()
        elif castlingtest3()==True:
            file=open('castling3.txt','a')
            file.write('True__True\n')
            file.close()
        else:
            file=open('castling3.txt','a')
            file.write('False__False\n')
            file.close()   
        if b['text']=='♖'and b['fg']==color4 and (b['bg']==color5 or b['bg']==color6):
            file=open('castling4.txt','a')
            file.write('False__False\n')
            file.close()
        elif castlingtest4()==True:
            file=open('castling4.txt','a')
            file.write('True__True\n')
            file.close()
        else:
            file=open('castling4.txt','a')
            file.write('False__False\n')
            file.close()   

def castlingtest1():
    a=open('castling1.txt','r')
    t=a.readlines()
    a.close()
    t.reverse()
    t=t[0]
    if t=='True__True\n':
        return True
    else:
        return False

def castlingtest2():
    a=open('castling2.txt','r')
    t=a.readlines()
    a.close()
    t.reverse()
    t=t[0]
    if t=='True__True\n':
        return True
    else:
        return False

def castlingtest3():
    a=open('castling3.txt','r')
    t=a.readlines()
    a.close()
    t.reverse()
    t=t[0]
    if t=='True__True\n':
        return True
    else:
        return False

def castlingtest4():
    a=open('castling4.txt','r')
    t=a.readlines()
    a.close()
    t.reverse()
    t=t[0]
    if t=='True__True\n':
        return True
    else:
        return False

def colorname(a):
    x=list(a)
    x.reverse()
    x.pop(0)
    x.reverse()
    s=''
    for i in x:
        s=s+i
    return s

def new(button,button__,tkk):
    button__['fg']=KEY
    a=button['text']
    b=a[0]
    button__['text']=b

def king(b1):
    if b1['fg']==color3 and castlingtest1()==True and pos1[(7,2)]['text']==' ' and pos1[(7,3)]['text']==' ' and pos1[(7,4)]['text']==' ':
        if showcolor==True:
                    pos1[(7,3)]['bg']=color6
        special.append(pos1[(7,3)])
    if b1['fg']==color3 and castlingtest2()==True and pos1[(7,6)]['text']==' ' and pos1[(7,7)]['text']==' ' :
        if showcolor==True:
                    pos1[(7,7)]['bg']=color6
        special.append(pos1[(7,7)])
    if b1['fg']==color4 and castlingtest4()==True and pos1[(0,6)]['text']==' ' and pos1[(0,7)]['text']==' ':
        if showcolor==True:
                    pos1[(0,7)]['bg']=color6
        special.append(pos1[(0,7)])
    if b1['fg']==color4 and castlingtest3()==True and pos1[(0,2)]['text']==' ' and pos1[(0,3)]['text']==' ' and pos1[(0,4)]['text']==' ':
        if showcolor==True:
                    pos1[(0,3)]['bg']=color6
        special.append(pos1[(0,3)])
    bpos=pos[b1]
    b=bpos[0]
    c=bpos[1]
    try:
        n=b+1
        l=c
        m=0
        if n<=8 and n>=0 and l<=8 and l>=1:
            m=(n,l)
        b2=pos1[m]
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
        elif b2['fg']!=b1['fg']:
            if showcolor==True:
                    b2['bg']=color5
            posmoves.append(b2)
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        n=b-1
        l=c
        m=0
        if n<=8 and n>=0 and l<=8 and l>=1:
            m=(n,l)
        b2=pos1[m]
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
        elif b2['fg']!=b1['fg']:
            if showcolor==True:
                    b2['bg']=color5
            posmoves.append(b2)
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        n=b
        l=c+1
        m=0
        if n<=8 and n>=0 and l<=8 and l>=1:
            m=(n,l)
        b2=pos1[m]
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
        elif b2['fg']!=b1['fg']:
            if showcolor==True:
                    b2['bg']=color5
            posmoves.append(b2)
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        n=b
        l=c-1
        m=0
        if n<=8 and n>=0 and l<=8 and l>=1:
            m=(n,l)
        b2=pos1[m]
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
        elif b2['fg']!=b1['fg']:
            if showcolor==True:
                    b2['bg']=color5
            posmoves.append(b2)
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        n=b+1
        l=c+1
        m=0
        if n<=8 and n>=0 and l<=8 and l>=1:
            m=(n,l)
        b2=pos1[m]
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
        elif b2['fg']!=b1['fg']:
            if showcolor==True:
                    b2['bg']=color5
            posmoves.append(b2)
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        n=b+1
        l=c-1
        m=0
        if n<=8 and n>=0 and l<=8 and l>=1:
            m=(n,l)
        b2=pos1[m]
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
        elif b2['fg']!=b1['fg']:
            if showcolor==True:
                    b2['bg']=color5
            posmoves.append(b2)
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        n=b-1
        l=c+1
        m=0
        if n<=8 and n>=0 and l<=8 and l>=1:
            m=(n,l)
        b2=pos1[m]
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
        elif b2['fg']!=b1['fg']:
            if showcolor==True:
                    b2['bg']=color5
            posmoves.append(b2)
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        n=b-1
        l=c-1
        m=0
        if n<=8 and n>=0 and l<=8 and l>=1:
            m=(n,l)
        b2=pos1[m]
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
        elif b2['fg']!=b1['fg']:
            if showcolor==True:
                    b2['bg']=color5
            posmoves.append(b2)
    except:
        pass

def knight(b1):
    bpos=pos[b1]
    k=bpos[0]+2
    l=bpos[1]+1
    n=(k,l)
    try:
        b2=pos1[n]
        if b2['fg']!=b1['fg']:
            if showcolor==True:
                b2['bg']=color5
            posmoves.append(b2)
        if b2['fg']==color1:
            if showcolor==True:
                b2['bg']=color6
            posmoves.append(b2)
    except:
        pass
    k=bpos[0]-2
    l=bpos[1]+1
    n=(k,l)
    try:
        b2=pos1[n]
        if b2['fg']!=b1['fg']:
            if showcolor==True:
                b2['bg']=color5
            posmoves.append(b2)
        if b2['fg']==color1:
            if showcolor==True:
                b2['bg']=color6
            posmoves.append(b2)
    except:
        pass
    k=bpos[0]+2
    l=bpos[1]-1
    n=(k,l)
    try:
        b2=pos1[n]
        if b2['fg']!=b1['fg']:
            if showcolor==True:
                b2['bg']=color5
            posmoves.append(b2)
        if b2['fg']==color1:
            if showcolor==True:
                b2['bg']=color6
            posmoves.append(b2)
    except:
        pass
    k=bpos[0]-2
    l=bpos[1]-1
    n=(k,l)
    try:
        b2=pos1[n]
        if b2['fg']!=b1['fg']:
            if showcolor==True:
                b2['bg']=color5
            posmoves.append(b2)
        if b2['fg']==color1:
            if showcolor==True:
                b2['bg']=color6
            posmoves.append(b2)
    except:
        pass
    k=bpos[0]+1
    l=bpos[1]+2
    n=(k,l)
    try:
        b2=pos1[n]
        if b2['fg']!=b1['fg']:
            if showcolor==True:
                b2['bg']=color5
            posmoves.append(b2)
        if b2['fg']==color1:
            if showcolor==True:
                b2['bg']=color6
            posmoves.append(b2)
    except:
        pass
    k=bpos[0]+1
    l=bpos[1]-2
    n=(k,l)
    try:
        b2=pos1[n]
        if b2['fg']!=b1['fg']:
            if showcolor==True:
                b2['bg']=color5
            posmoves.append(b2)
        if b2['fg']==color1:
            if showcolor==True:
                b2['bg']=color6
            posmoves.append(b2)
    except:
        pass
    k=bpos[0]-1
    l=bpos[1]+2
    n=(k,l)
    try:
        b2=pos1[n]
        if b2['fg']!=b1['fg']:
            if showcolor==True:
                b2['bg']=color5
            posmoves.append(b2)
        if b2['fg']==color1:
            if showcolor==True:
                b2['bg']=color6
            posmoves.append(b2)
    except:
        pass
    k=bpos[0]-1
    l=bpos[1]-2
    n=(k,l)
    try:
        b2=pos1[n]
        if b2['fg']!=b1['fg']:
            if showcolor==True:
                b2['bg']=color5
            posmoves.append(b2)
        if b2['fg']==color1:
            if showcolor==True:
                b2['bg']=color6
            posmoves.append(b2)
    except:
        pass

def rook(b1):
    bpos=pos[b1]
    b=bpos[0]
    c=bpos[1]
    try:
        while b<=9:
            b+=1
            l=(b,c)
            b2=pos1[l]
            if b2['text']==' ':
                if showcolor==True:
                    b2['bg']=color6
                posmoves.append(b2)
            elif b2['fg']!=b1['fg']:
                if showcolor==True:
                    b2['bg']=color5
                posmoves.append(b2)
                break
            else:
                break
    except:
        pass
    b2=''
    b=bpos[0]
    c=bpos[1]
    try:
        while b>=0:
            b=b-1
            l=(b,c)
            b2=pos1[l]
            if b2['text']==' ':
                if showcolor==True:
                    b2['bg']=color6
                posmoves.append(b2)
            elif b2['fg']!=b1['fg']:
                if showcolor==True:
                    b2['bg']=color5
                posmoves.append(b2)
                break
            else:
                break
    except:
        pass
    b2=''
    b=bpos[0]
    c=bpos[1]
    try:
        while c<=9:
            c+=1
            l=(b,c)
            b2=pos1[l]
            if b2['text']==' ':
                if showcolor==True:
                    b2['bg']=color6
                posmoves.append(b2)
            elif b2['fg']!=b1['fg']:
                if showcolor==True:
                    b2['bg']=color5
                posmoves.append(b2)
                break
            else:
                break
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    b2=''
    try:
        while c>=0:
            c=c-1
            l=(b,c)
            b2=pos1[l]
            if b2['text']==' ':
                if showcolor==True:
                    b2['bg']=color6
                posmoves.append(b2)
            elif b2['fg']!=b1['fg']:
                if showcolor==True:
                    b2['bg']=color5
                posmoves.append(b2)
                break
            else:
                break
    except:
        pass

def bishop(b1):
    bpos=pos[b1]
    b=bpos[0]
    c=bpos[1]
    try:
        while b<=8 and c<=7:
            b+=1
            c+=1
            l=(b,c)
            b2=pos1[l]
            if b2['text']==' ':
                if showcolor==True:
                    b2['bg']=color6
                posmoves.append(b2)
            elif b2['fg']!=b1['fg']:
                if showcolor==True:
                    b2['bg']=color5
                posmoves.append(b2)
                break
            else:
                break
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        while b<=8 and c>=2:
            b+=1
            c-=1
            l=(b,c)
            b2=pos1[l]
            if b2['text']==' ':
                if showcolor==True:
                    b2['bg']=color6
                posmoves.append(b2)
            elif b2['fg']!=b1['fg']:
                if showcolor==True:
                    b2['bg']=color5
                posmoves.append(b2)
                break
            else:
                break
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        while b>=0 and c<=7:
            b-=1
            c+=1
            l=(b,c)
            b2=pos1[l]
            if b2['text']==' ':
                if showcolor==True:
                    b2['bg']=color6
                posmoves.append(b2)
            elif b2['fg']!=b1['fg']:
                if showcolor==True:
                    b2['bg']=color5
                posmoves.append(b2)
                break
            else:
                break
    except:
        pass
    b=bpos[0]
    c=bpos[1]
    try:
        while b>=0 and c>=2:
            b=b-1
            c=c-1
            l=(b,c)
            b2=pos1[l]
            if b2['text']==' ':
                if showcolor==True:
                    b2['bg']=color6
                posmoves.append(b2)
            elif b2['fg']!=b1['fg']:
                if showcolor==True:
                    b2['bg']=color5
                posmoves.append(b2)
                break
            else:
                break
    except:
        pass

def queen(b1):
    rook(b1)
    bishop(b1)

def pawn(b1):
    b2,b3,b4,b5='','','',''
    bpos=pos[b1]
    if b1['fg']==color3:
        k=bpos[0]-1
        l=bpos[1]
        n=(k,l)
        try:
            b2=pos1[n]
        except:
            del(b2)
        k=bpos[0]-2
        l=bpos[1]
        n=(k,l)
        try:
            b3=pos1[n]
        except:
            del(b3)
        k=bpos[0]-1
        l=bpos[1]-1
        n=(k,l)
        try:
            b4=pos1[n]
        except:
            del(b4)
        k=bpos[0]-1
        l=bpos[1]+1
        n=(k,l)
        try:
            b5=pos1[n]
        except:
            del(b5)
    if b1['fg']==color4:
        k=bpos[0]+1
        l=bpos[1]
        n=(k,l)
        try:
            b2=pos1[n]
        except:
            del(b2)
        k=bpos[0]+2
        l=bpos[1]
        n=(k,l)
        try:
            b3=pos1[n]
        except:
            del(b3)
        k=bpos[0]+1
        l=bpos[1]-1
        n=(k,l)
        try:
            b4=pos1[n]
        except:
            del(b4)
        k=bpos[0]+1
        l=bpos[1]+1
        n=(k,l)
        try:
            b5=pos1[n]
        except:
            del(b5)
    ppaw={color3:6,color4:1}
    colour=b1['fg']
    pos__1=ppaw[colour]
    try:
        if b2['text']==' ':
            if showcolor==True:
                    b2['bg']=color6
            posmoves.append(b2)
            if b3['text']==' ' and pos[b1][0]==pos__1:
                if showcolor==True:
                    b3['bg']=color6
                posmoves.append(b3)
    except:
        pass
    try:
        if b4['fg']!=color1 and b1['fg']!=b4['fg']:
            if showcolor==True:
                    b4['bg']=color5
            posmoves.append(b4)
    except:
        pass
    try:
        if b5['fg']!=color1 and b1['fg']!=b5['fg']:
            if showcolor==True:
                    b5['bg']=color5
            posmoves.append(b5)
    except:
        pass
def moves(t,b1):
    global posmoves
    posmoves=[]
    special=[]
    if t=='♟':
        pawn(b1)
    if t=='♖' or t=='♜':
        rook(b1)
    if t=='♝':
        bishop(b1)
    if t=='♚':
        king(b1)
    if t=='♛':
        queen(b1)
    if t=='♞':
        knight(b1)
    b1['bg']=color7

def returntocolor():
    for i in range(1,65):
        p=aa[i]
        if (i %8)==0:
            if (i//8)%2==1:
                p['bg']=color2
            else:
                p['bg']=color1
        elif (i//8)%2==0:
            if i%2==0:
                p['bg']=color2
            else:
                p['bg']=color1
        else:
            if i%2==1:
                p['bg']=color2
            else:
                p['bg']=color1
        if p['text']==' ':
            p['fg']=color1

def undo():
    global bwbw
    try:
        undo_()
    except:
        if bwbw==color3:
            bwbw=color4
        else:
            bwbw=color3

def undo_() :
    global bwbw
    if bwbw==color4:
        bwbw=color3
    else:
        bwbw=color4    
    files=open('moves.txt','r')
    b=files.read()
    b=b.split('\n')
    b.reverse()
    b.pop(0)
    b.pop(0)
    b.pop(0)
    m=b[0]
    n=b[1]
    for i in range(1,65):
            p=aa[i]
            q=n[i-1]
            q=x1[q]
            r=m[i-1]
            r=y1[r]
            p['fg']=r
            p['text']=q
    files.close()
    b.reverse()
    xx=[]
    for i in b:
        cc=i+'\n'
        xx.append(cc)
    b=xx
    files=open('moves.txt','w')
    files.writelines(b)
    files.close()
    
    file=open('castling1.txt','r')
    a=file.readlines()
    file.close()
    a.reverse()
    a.pop(0)
    a.reverse()
    file=open('castling1.txt','w')
    file.writelines(a)
    file.close()
    file=open('castling2.txt','r')
    a=file.readlines()
    file.close()
    a.reverse()
    a.pop(0)
    a.reverse()
    file=open('castling2.txt','w')
    file.writelines(a)
    file.close()
    file=open('castling3.txt','r')
    a=file.readlines()
    file.close()
    a.reverse()
    a.pop(0)
    a.reverse()
    file=open('castling3.txt','w')
    file.writelines(a)
    file.close()
    file=open('castling4.txt','r')
    a=file.readlines()
    file.close()
    a.reverse()
    a.pop(0)
    a.reverse()
    file=open('castling4.txt','w')
    file.writelines(a)
    file.close()

def check(p):
    global showcolor,posmoves,xxxxx
    posmoves=[]
    for i in range(1,65):
        butt=aa[i]
        x=showcolor
        showcolor=False
        if butt['text']!='♚':
            moves(butt['text'],butt)
            returntocolor()
        for j in posmoves:
                if j['text']=='♚':
                    if j['fg']!=p['fg']:
                        showwarning('warning','Check')
                        if j['fg']==color3:
                            file=open('castling1.txt','w')
                            file.write('False__False\n')
                            file.close()
                            file=open('castling2.txt','w')
                            file.write('False__False\n')
                            file.close()
                        if j['fg']==color4:
                            file=open('castling3.txt','w')
                            file.write('False__False\n')
                            file.close()
                            file=open('castling4.txt','w')
                            file.write('False__False\n')
                            file.close()
                    elif j['fg']==p['fg'] and xxxxx==False:
                        showwarning('warning','Check invalid move')
                        undo()
                    posmoves=[]
                    special=[]
        showcolor=x
        xxxxx=False

def write():
    files=open('moves.txt','a')
    m=''
    n=''
    for i in range(1,65):
                            p=aa[i]
                            q=p['text']
                            q=x[q]
                            r=p['fg'];
                            r=y[r]
                            m+=q
                            n+=r
    m+='\n'
    n+='\n'
    files.write(m)
    files.write(n)
    files.close()

def invalidcheck(bbb,bgg,tk=None):
    global bwbw,xxxxx
    if bbb in posmoves :
        if bwbw==color3:
            bwbw=color4
        else:
            bwbw=color3
    elif bbb in special:
        if bwbw==color3:
            bwbw=color4
        else:
            bwbw=color3
        if bbb==button63:
            button62['text']='♖'
            button62['fg']=color3
            button64['text']=' '
            xxxxx=True
        if bbb==button59:
            button60['text']='♖'
            button60['fg']=color3
            button57['text']=' '
            xxxxx=True
        if bbb==button3:
            button4['text']='♖'
            button4['fg']=color4
            button1['text']=' '
            xxxxx=True
        if bbb==button7:
            button6['text']='♖'
            button6['fg']=color4
            button8['text']=' '
            xxxxx=True
    elif bgg!=color7:
        if bwbw==color3:
            bwbw=color4
        else:
            bwbw=color3
        showwarning('Invalid','Invalid Move : Please Enter the valid Move.')
        try:
            tk.destroy()
        except:
            pass
        undo()

def showonoff(buttons):
    global showcolor
    dicta={'Red':'Green','Green':'Red'}
    buttons['fg']=dicta[buttons['fg']]
    showcolor=not showcolor

def concolor(listt,buttons,dict1):
    global color1,color2,color3,color4,color5,color6,color7
    x=askcolor()
    buttons['bg']=x[1]
    lll=[dict1[1]['bg']+'\n',dict1[2]['bg']+'\n',dict1[3]['bg']+'\n',dict1[4]['bg']+'\n',dict1[5]['bg']+'\n',dict1[6]['bg']+'\n',dict1[7]['bg']+'\n']
    files=open('configuration.txt','w')
    files.writelines(lll)
    files.close()

def okexecute(dict1,a):
    lll=[dict1[1]['bg']+'\n',dict1[2]['bg']+'\n',dict1[3]['bg']+'\n',dict1[4]['bg']+'\n',dict1[5]['bg']+'\n',dict1[6]['bg']+'\n',dict1[7]['bg']+'\n']
    files=open('configuration.txt','w')
    files.writelines(lll)
    files.close()
    showinfo('Information','Open The Game Again To Get The Configuration')
    a.destroy()

def cancelexecute(a):
    a.destroy()

def configure():
    global color1,color2,color3,color4,color5,color6,color7
    files=open('configuration.txt','r')
    l=files.readlines()
    files.close()
    tk=Tk()
    tk.geometry('500x500')
    tk.title('Color Configuration')
    tk.config(bg='skyblue')
    label1=Label(tk,bg='Powder Blue',text='Board Color 1                    ',font=('Arial 15 bold'))
    label1.grid(row=1,column=1)
    label2=Label(tk,bg='Powder Blue',text='Board Color 2                    ',font=('Arial 15 bold'))
    label2.grid(row=2,column=1)
    label3=Label(tk,bg='Powder Blue',text='Player Color 1                    ',font=('Arial 15 bold'))
    label3.grid(row= 3,column=1)
    label4=Label(tk,bg='Powder Blue',text='Player Color 2                    ',font=('Arial 15 bold'))
    label4.grid(row=4,column=1)
    label5=Label(tk,bg='Powder Blue',text='Moves Color 1                    ',font=('Arial 15 bold'))
    label5.grid(row=5,column=1)
    label6=Label(tk,bg='Powder Blue',text='Moves Color 2                    ',font=('Arial 15 bold'))
    label6.grid(row=6,column=1)
    label7=Label(tk,bg='Powder Blue',text='Moves Color 3                    ',font=('Arial 15 bold'))
    label7.grid(row=7,column=1)
    button1=Button(tk,height=1,width=9,bd=3,bg=color1,command=lambda:concolor(l,button1,dicty))
    button2=Button(tk,height=1,width=9,bd=3,bg=color2,command=lambda:concolor(l,button2,dicty))
    button3=Button(tk,height=1,width=9,bd=3,bg=color3,command=lambda:concolor(l,button3,dicty))
    button4=Button(tk,height=1,width=9,bd=3,bg=color4,command=lambda:concolor(l,button4,dicty))
    button5=Button(tk,height=1,width=9,bd=3,bg=color5,command=lambda:concolor(l,button5,dicty))
    button6=Button(tk,height=1,width=9,bd=3,bg=color6,command=lambda:concolor(l,button6,dicty))
    button7=Button(tk,height=1,width=9,bd=3,bg=color7,command=lambda:concolor(l,button7,dicty))
    button1.grid(row=1,column= 3,pady=10)
    button2.grid(row=2,column= 3,pady=10)
    button3.grid(row=3,column= 3,pady=10)
    button4.grid(row=4,column= 3,pady=10)
    button5.grid(row=5,column= 3,pady=10)
    button6.grid(row=6,column= 3,pady=10)
    button7.grid(row=7,column= 3,pady=10)
    button8=Button(tk,text='ok',height=1,width=7,bd=5,bg='Powder blue',command=lambda:okexecute(dicty,tk))
    button8.grid(row=8,column=1,pady=10)
    button9=Button(tk,text='cancel',height=1,width=7,bd=5,bg='Powder blue',command=lambda:cancelexecute(tk))
    button9.grid(row=8,column= 2,pady=10)
    dicty={1:button1,2:button2,3:button3,4:button4,5:button5,6:button6,7:button7}

def gamesave(a,b,c,l,m):
    x=a.get()
    y=b.get()
    z=c.get()
    t=x+y+z+'.txt'
    files=open(t,'w')
    files.writelines(l)
    files.close()
    m.destroy()

def gameopen(a,b,c,l,m):
    x=a.get()
    y=b.get()
    z=c.get()
    t=x+y+z+'.txt'
    files=open(t,'r')
    l=files.readlines()
    files.close()
    files=open('moves.txt','w')
    files.write('''rhbqkbhrpppppppp                                pppppppprhbqkbhr
ggggggggggggggggppppppppppppppppppppppppppppwpppwwwwwwwwwwwwwwww\n''')
    files.writelines(l)
    files.write('''rhbqkbhrpppppppp                                pppppppprhbqkbhr
ggggggggggggggggppppppppppppppppppppppppppppwpppwwwwwwwwwwwwwwww\n''')
    files.close()
    m.destroy()
    undo()

def save_open_game(buttons):
    files=open('moves.txt','r')
    l=files.readlines()
    files.close()
    tk=Tk()
    tk.config(bg='Powder Blue')
    tk.title('Save Game')
    tk.geometry('500x400+0+0')
    a=Entry(tk,width=25)
    a.grid(row=1,column= 3)
    b=Entry(tk,width=25)
    b.grid(row= 5,column= 3)
    c=Entry(tk,width=25)
    c.grid(row=9,column= 3)
    Label(tk,text='Player1',bg='Powder Blue',font=('Arial 15 bold')).grid(row=1,column=1,pady=20)
    Label(tk,text='Player2',bg='Powder Blue',font=('Arial 15 bold')).grid(row=5,column=1,pady=20)
    Label(tk,text='''Game Number
(**to identify the
particular game)''',bg='Powder Blue',font=('Arial 15 bold')).grid(row=9,column=1,pady=20)
    if buttons['text']=='Save Game':
        Button(tk,text='ok',bg='Powder Blue',height=1,width=7,bd=3,command=lambda:(gamesave(a,b,c,l,tk))).grid(row=11,column=2,pady=20)
    if buttons['text']=='Open Game':
        Button(tk,text='ok',bg='Powder Blue',height=1,width=7,bd=3,command=lambda:(gameopen(a,b,c,l,tk))).grid(row=11,column=2,pady=20)

def cheker(buttons,S):
    try:
        cheker_(buttons,S)
    except:
        pass

def cheker_(buttons,S):
                global click,xxxxx,labeling1,labeling2,labeling3,labeling4,labeling5,labeling6,labeling7,labeling8
                global SELECTED_KEY
                global KEY,UNDO_1,UNDO_2,BUT1,BUT2,FG1,FG2
                global aa,bwbw,posmoves,color3,color4,button65,button66,button67,button68,button69,button70,button71
                pppp=buttons
                aaa=pppp['text']
                bbb=pppp['bg']
                if S==' ' and click == True and buttons['text']!=' ':
                    aa[65]['command']=lambda:(pass_())
                    if buttons['fg']==bwbw:
                        SELECTED_KEY=buttons['text'] 
                        buttons['text'] = ' '
                        KEY=buttons['fg']
                        BUT1=buttons
                        FG1=KEY
                        moves(aaa,pppp)
                        labeling1=Label(main,text='rules',fg= 'Powder Blue' ,font = ('Arial 11 bold'),bg='black' ,height = 3 , width =13)
                        labeling2=Label(main,text='''REMOVE
COLOURERROR''',fg= 'Powder Blue' ,font = ('Arial 11 bold'),bg='black' ,height = 3 , width =13)
                        labeling3=Label(main,text='OPENGAME',fg= 'Powder Blue' ,font = ('Arial 11 bold'),bg='black' ,height = 3 , width =13)
                        labeling4=Label(main,text='UNDO',fg= 'Powder Blue' ,font = ('Arial 11 bold'),bg='black' ,height = 3 , width =13)
                        labeling5=Label(main,text='SHOWMOVES',fg= 'Powder Blue' ,font = ('Arial 11 bold'),bg='black' ,height = 3 , width =13)
                        labeling6=Label(main,text='CONFIGURE',fg= 'Powder Blue' ,font = ('Arial 11 bold'),bg='black' ,height = 3 , width =13)
                        labeling7=Label(main,text='SAVEGAME',fg= 'Powder Blue' ,font = ('Arial 11 bold'),bg='black' ,height = 3 , width =13)
                        labeling1.grid(row=1,column=9)
                        labeling2.grid(row=2,column=9)
                        labeling3.grid(row= 3 ,column=9)
                        labeling4.grid(row=4,column=9)
                        labeling5.grid(row=5,column=9)
                        labelingeling6.grid(row=6,column=9)
                        labeling7.grid(row=7,column=9)
                    elif buttons['fg']!=bwbw :
                        showwarning('Warning','Others move')
                    
                if S=='♟' and buttons['font']=='Arial 26 bold' and click==True:
                    labeling1['width']=0
                    labeling1['text']=''
                    labeling1.grid(row=1,column=10)
                    labeling2['width']=0
                    labeling2['text']=''
                    labeling2.grid(row=2,column=10)
                    labeling3['width']=0
                    labeling3['text']=''
                    labeling3.grid(row= 8,column=10)
                    labeling4['width']=0
                    labeling4['text']=''
                    labeling4.grid(row=4,column=10)
                    labeling5['width']=0
                    labeling5['text']=''
                    labeling5.grid(row=5,column=10)
                    labeling6['width']=0
                    labeling6['text']=''
                    labeling6.grid(row=6,column=10)
                    labeling7['width']=0
                    labeling7['text']=''
                    labeling7.grid(row=7,column=10)
                    aa[65]['command']=lambda:(undo())
                    SELECTED_KEY=' '
                    a=buttons
                    opt=Tk()
                    button111 = Button(opt,text='♖  rook',fg= color5 ,font = ('Arial 15 bold'),bg= color1 ,height =1 , width =10, command=lambda:new(button111,a,opt))
                    button111 .grid(row= 0 , column=1 )
                    button211 = Button(opt,text='♞ knight',fg= color5 ,font = ('Arial 15 bold'),bg= color1 ,height =1 , width =10, command=lambda:new(button211,a,opt))
                    button211 .grid(row=1 , column=1 )
                    button311 = Button(opt,text='♝ bishop',fg= color5 ,font = ('Arial 15 bold'),bg= color1 ,height =1 , width =10, command=lambda:new(button311,a,opt))
                    button311 .grid(row= 2 , column=1)
                    button411 = Button(opt,text='♛ queen',fg= color5 ,font = ('Arial 15 bold'),bg= color1 ,height =1 , width =10, command=lambda:new(button411,a,opt))
                    button411 .grid(row= 3 , column=1 )
                    returntocolor()
                    opt.mainloop()
                    if click==True:
                        write()
                        invalidcheck(buttons,bbb,opt)
                        castlingperm(buttons)
                        returntocolor()
                        check(buttons)
                elif S!=' ' and click ==True:
                        labeling1['width']=0
                        labeling1['text']=''
                        labeling1.grid(row=1,column=10)
                        labeling2['width']=0
                        labeling2['text']=''
                        labeling2.grid(row=2,column=10)
                        labeling3['width']=0
                        labeling3['text']=''
                        labeling3.grid(row= 8,column=10)
                        labeling4['width']=0
                        labeling4['text']=''
                        labeling4.grid(row=4,column=10)
                        labeling5['width']=0
                        labeling5['text']=''
                        labeling5.grid(row=5,column=10)
                        labeling6['width']=0
                        labeling6['text']=''
                        labeling6.grid(row=6,column=10)
                        labeling7['width']=0
                        labeling7['text']=''
                        labeling7.grid(row=7,column=10)
                        aa[65]['command']=lambda:(undo())
                        BUT2=buttons
                        FG2=buttons['fg']
                        UNDO_1=SELECTED_KEY
                        UNDO_2=buttons['text']
                        buttons['text']=SELECTED_KEY
                        SELECTED_KEY=' '
                        buttons['fg']=KEY
                        files=open('moves.txt','a')
                        m=''
                        n=''
                        write()
                        invalidcheck(buttons,bbb) 
                        castlingperm(buttons)
                        returntocolor()
                        check(buttons)

def get_connected_linkedin():
        new = 1
        url = "https://www.linkedin.com/in/girish-kumar-goyal-189152198"
        wb.open(url,new=new,autoraise=True)

def get_connected_instagram():
        new = 1
        url = "https://www.instagram.com/invites/contact/?!=hnukdweg81ch&utm_content=ad5j31z"
        wb.open(url,new=new,autoraise=True)

def get_connected_github():
        new = 1
        url = "https://github.com/Girish-1-Goyal"
        wb.open(url,new=new,autoraise=True)

def exit_func():
    exit = askyesno('Exit','Do you want to really Exit')
    try:
        if exit is True:
            main.destroy()
        else:
            return
    except:
        return

def main_fun():
    ########################################## Global Variables ##########################################
    global special,x,x1,y,y1,aa,pos,pos1,SELECTED_KEY,KEY,color1,color2,color3,color4
    global color5,color6,color7,bwbw,showcolor,posmoves,eating,main,button1,button2
    global button3,button4,button5,button6,button7,button8,button9,button10,button11
    global button12,button13,button14,button15,button16,button17,button18,button19
    global button20,button21,button22,button23,button24,button25,button26,button27
    global button28,button29,button30,button31,button32,button33,button34,button35
    global button36,button37,button38,button39,button40,button41,button42,button43
    global button44,button45,button46,button47,button48,button49,button50,button51
    global button52,button53,button54,button55,button56,button57,button58,button59
    global button60,button61,button62,button63,button64,button65,button66,button67,button68,button69,button70,button71

    files=open('configuration.txt','r')
    l=files.readlines()
    files.close()
    color1=colorname(l[0])
    color2=colorname(l[1])
    color3=colorname(l[2])
    color4=colorname(l[3])
    color5=colorname(l[4])
    color6=colorname(l[5])
    color7=colorname(l[6])
    file=open('castling1.txt','w')
    file.write('True__True\n')
    file.close()
    file=open('castling2.txt','w')
    file.write('True__True\n')
    file.close()
    file=open('castling3.txt','w')
    file.write('True__True\n')
    file.close()
    file=open('castling4.txt','w')
    file.write('True__True\n')
    file.close()
    
    global click,labeling1,labeling2,labeling3,labeling4
    global labeling5,labeling6,labeling7,labeling8

    click=True
    main=Tk()
    main.title("CHESS GAME")
    main.geometry('1440x890+0+0')
    main.resizable(width=False,height=False)
    main.config(bg='Powder Blue')
    main.icon_set = Image("photo",file="chess.png")
    main.call('wm','iconphoto',main._w,main.icon_set)
    time=datetime.now()
    
    x={'♞':'h','♖':'r','♝':'b','♟':'p','♚':'k','♛':'q',' ':' ','♜':'R'}
    x1={'h':'♞','r':'♖','b':'♝','p':'♟','k':'♚','q':'♛',' ':' ','R':'♜'}
    y={color4:'g',color1:'p',color3:'w'}
    y1={'g':color4,'p':color1,'w':color3}
    
    click = True
    files=open('moves.txt','w')
    files.write('''Correct Move\n''')
    files.close()
    posmoves=[]
    special=[]
    eating=[]
    showcolor=False
    SELECTED_KEY=' '
    KEY=' '
    bwbw=color3
    buttons=StringVar()
    button1 = Button(main,text='♜',fg= color4 ,font = ('Arial 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button1 ,SELECTED_KEY))
    button1 .grid(row= 0 , column=1 ,)
    button2 = Button(main,text='♞',fg= color4 ,font = ('Arial 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button2 ,SELECTED_KEY))
    button2 .grid(row= 0 , column= 2 ,)
    button3 = Button(main,text='♝',fg= color4 ,font = ('Arial 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button3 ,SELECTED_KEY))
    button3 .grid(row= 0 , column= 3 ,)
    button4 = Button(main,text='♛',fg= color4 ,font = ('Arial 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button4 ,SELECTED_KEY))
    button4 .grid(row= 0 , column= 4 ,)
    button5 = Button(main,text='♚',fg= color4 ,font = ('Arial 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button5 ,SELECTED_KEY))
    button5 .grid(row= 0 , column= 5 ,)
    button6 = Button(main,text='♝',fg= color4 ,font = ('Arial 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button6 ,SELECTED_KEY))
    button6 .grid(row= 0 , column= 6 ,)
    button7 = Button(main,text='♞',fg= color4 ,font = ('Arial 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button7 ,SELECTED_KEY))
    button7 .grid(row= 0 , column= 7 ,)
    button8 = Button(main,text='♖',fg= color4 ,font = ('Arial 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button8 ,SELECTED_KEY))
    button8 .grid(row= 0 , column= 8 ,)
    button9 = Button(main,text='♟',fg= color4 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button9 ,SELECTED_KEY))
    button9 .grid(row=1 , column=1 ,)
    button10 = Button(main,text='♟',fg= color4 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button10 ,SELECTED_KEY))
    button10 .grid(row=1 , column= 2 ,)
    button11 = Button(main,text='♟',fg= color4 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button11 ,SELECTED_KEY))
    button11 .grid(row=1 , column= 3 ,)
    button12 = Button(main,text='♟',fg= color4 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button12 ,SELECTED_KEY))
    button12 .grid(row=1 , column= 4 ,)
    button13 = Button(main,text='♟',fg= color4 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button13 ,SELECTED_KEY))
    button13 .grid(row=1 , column= 5 ,)
    button14 = Button(main,text='♟',fg= color4 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button14 ,SELECTED_KEY))
    button14 .grid(row=1 , column= 6 ,)
    button15 = Button(main,text='♟',fg= color4 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button15 ,SELECTED_KEY))
    button15 .grid(row=1 , column= 7 ,)
    button16 = Button(main,text='♟',fg= color4 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button16 ,SELECTED_KEY))
    button16 .grid(row=1 , column= 8 ,)
    button17 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button17 ,SELECTED_KEY))
    button17 .grid(row= 2 , column=1 ,)
    button18 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button18 ,SELECTED_KEY))
    button18 .grid(row= 2 , column= 2 ,)
    button19 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button19 ,SELECTED_KEY))
    button19 .grid(row= 2 , column= 3 ,)
    button20 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button20 ,SELECTED_KEY))
    button20 .grid(row= 2 , column= 4 ,)
    button21 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button21 ,SELECTED_KEY))
    button21 .grid(row= 2 , column= 5 ,)
    button22 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button22 ,SELECTED_KEY))
    button22 .grid(row= 2 , column= 6 ,)
    button23 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button23 ,SELECTED_KEY))
    button23 .grid(row= 2 , column= 7 ,)
    button24 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button24 ,SELECTED_KEY))
    button24 .grid(row= 2 , column= 8 ,)
    button25 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button25 ,SELECTED_KEY))
    button25 .grid(row= 3 , column=1 ,)
    button26 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button26 ,SELECTED_KEY))
    button26 .grid(row= 3 , column= 2 ,)
    button27 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button27 ,SELECTED_KEY))
    button27 .grid(row= 3 , column= 3 ,)
    button28 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button28 ,SELECTED_KEY))
    button28 .grid(row= 3 , column= 4 ,)
    button29 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button29 ,SELECTED_KEY))
    button29 .grid(row= 3 , column= 5 ,)
    button30 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button30 ,SELECTED_KEY))
    button30 .grid(row= 3 , column= 6 ,)
    button31 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button31 ,SELECTED_KEY))
    button31 .grid(row= 3 , column= 7 ,)
    button32 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button32 ,SELECTED_KEY))
    button32 .grid(row= 3 , column= 8 ,)
    button33 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button33 ,SELECTED_KEY))
    button33 .grid(row= 4 , column=1 ,)
    button34 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button34 ,SELECTED_KEY))
    button34 .grid(row= 4 , column= 2 ,)
    button35 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button35 ,SELECTED_KEY))
    button35 .grid(row= 4 , column= 3 ,)
    button36 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button36 ,SELECTED_KEY))
    button36 .grid(row= 4 , column= 4 ,)
    button37 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button37 ,SELECTED_KEY))
    button37 .grid(row= 4 , column= 5 ,)
    button38 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button38 ,SELECTED_KEY))
    button38 .grid(row= 4 , column= 6 ,)
    button39 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button39 ,SELECTED_KEY))
    button39 .grid(row= 4 , column= 7 ,)
    button40 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button40 ,SELECTED_KEY))
    button40 .grid(row= 4 , column= 8 ,)
    button41 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button41 ,SELECTED_KEY))
    button41 .grid(row= 5 , column=1 ,)
    button42 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button42 ,SELECTED_KEY))
    button42 .grid(row= 5 , column= 2 ,)
    button43 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button43 ,SELECTED_KEY))
    button43 .grid(row= 5 , column= 3 ,)
    button44 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button44 ,SELECTED_KEY))
    button44 .grid(row= 5 , column= 4 ,)
    button45 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button45 ,SELECTED_KEY))
    button45 .grid(row= 5 , column= 5 ,)
    button46 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button46 ,SELECTED_KEY))
    button46 .grid(row= 5 , column= 6 ,)
    button47 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button47 ,SELECTED_KEY))
    button47 .grid(row= 5 , column= 7 ,)
    button48 = Button(main,text=' ',fg= color1 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button48 ,SELECTED_KEY))
    button48 .grid(row= 5 , column= 8 ,)
    button49 = Button(main,text='♟',fg= color3 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button49 ,SELECTED_KEY))
    button49 .grid(row= 6 , column=1 ,)
    button50 = Button(main,text='♟',fg= color3 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button50 ,SELECTED_KEY))
    button50 .grid(row= 6 , column= 2 ,)
    button51 = Button(main,text='♟',fg= color3 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button51 ,SELECTED_KEY))
    button51 .grid(row= 6 , column= 3 ,)
    button52 = Button(main,text='♟',fg= color3 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button52 ,SELECTED_KEY))
    button52 .grid(row= 6 , column= 4 ,)
    button53 = Button(main,text='♟',fg= color3 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button53 ,SELECTED_KEY))
    button53 .grid(row= 6 , column= 5 ,)
    button54 = Button(main,text='♟',fg= color3 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button54 ,SELECTED_KEY))
    button54 .grid(row= 6 , column= 6 ,)
    button55 = Button(main,text='♟',fg= color3 ,font = ('Times 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button55 ,SELECTED_KEY))
    button55 .grid(row= 6 , column= 7 ,)
    button56 = Button(main,text='♟',fg= color3 ,font = ('Times 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button56 ,SELECTED_KEY))
    button56 .grid(row= 6 , column= 8 ,)
    button57 = Button(main,text='♜',fg= color3 ,font = ('Arial 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button57 ,SELECTED_KEY))
    button57 .grid(row= 7 , column=1 ,)
    button58 = Button(main,text='♞',fg= color3 ,font = ('Arial 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button58 ,SELECTED_KEY))
    button58 .grid(row= 7 , column= 2 ,)
    button59 = Button(main,text='♝',fg= color3 ,font = ('Arial 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button59 ,SELECTED_KEY))
    button59 .grid(row= 7 , column= 3 ,)
    button60 = Button(main,text='♛',fg= color3 ,font = ('Arial 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button60 ,SELECTED_KEY))
    button60 .grid(row= 7 , column= 4 ,)
    button61 = Button(main,text='♚',fg= color3 ,font = ('Arial 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button61 ,SELECTED_KEY))
    button61 .grid(row= 7 , column= 5 ,)
    button62 = Button(main,text='♝',fg= color3 ,font = ('Arial 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button62 ,SELECTED_KEY))
    button62 .grid(row= 7 , column= 6 ,)
    button63 = Button(main,text='♞',fg= color3 ,font = ('Arial 26 bold'),bg= color2 ,height = 2 , width = 8, command=lambda:cheker(button63 ,SELECTED_KEY))
    button63 .grid(row= 7 , column= 7 ,)
    button64 = Button(main,text='♖',fg= color3 ,font = ('Arial 26 bold'),bg= color1 ,height = 2 , width = 8, command=lambda:cheker(button64 ,SELECTED_KEY))
    button64 .grid(row= 7 , column= 8 ,)
    frm1 = Frame(main,width=800,height=150,bd= 5,relief='solid')
    frm1.place(x=50,y=750)
    button65 = Button(frm1,text='Rules',fg= 'black' ,font = ('Arial 11 bold'),bg= 'skyblue' ,height = 3 , width =13, command=lambda:rules())
    button65 .grid(row= 0 , column=1 ,)
    button66 = Button(frm1,text='Move Check',fg= 'Red',font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13, command=lambda:showonoff(button66))
    button66 .grid(row= 0 , column=2 ,)
    button67 = Button(frm1,text='Configuration',fg= 'black' ,font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13, command=lambda:configure())
    button67 .grid(row= 0 , column=3 ,)
    button68 = Button(frm1,text='Save Game',fg= 'black' ,font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13, command=lambda:save_open_game(button68))
    button68 .grid(row= 0, column=4 ,)
    button69 = Button(frm1,text='Open Game',fg= 'black' ,font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13, command=lambda:save_open_game(button69))
    button69.grid(row= 0, column=5 ,)
    button71 = Button(frm1,text='Undo',fg= 'black' ,font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13, command=lambda:undo())
    button71.grid(row=0, column=7 ,)
    button72 = Button(frm1,text='''Join
LinkedIn''',fg= 'black' ,font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13,command=lambda:get_connected_linkedin())
    button72.grid(row= 0, column=8 ,)
    button73 = Button(frm1,text='''Join
GitHub''',fg= 'black' ,font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13,command=lambda:get_connected_github())
    button73.grid(row= 0, column=9 ,)
    button74 = Button(frm1,text='''Join 
Instagram''',fg= 'black' ,font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13,command=lambda:get_connected_instagram())
    button74.grid(row= 0, column=10 ,)

    button75 = Button(frm1,text='Exit',fg= 'black' ,font = ('Arial 11 bold'),bg='skyblue' ,height = 3 , width =13,command=lambda:exit_func())
    button75.grid(row= 0, column=11 ,)
    aa={65:button65,1 :button1 ,2 :button2 ,3 :button3 ,4 :button4 ,5 :button5 ,6 :button6 ,7 :button7 ,8 :button8 ,9 :button9 ,10 :button10 ,11 :button11 ,12 :button12 ,13 :button13 ,14 :button14 ,15 :button15 ,16 :button16 ,17 :button17 ,18 :button18 ,19 :button19 ,20 :button20 ,21 :button21 ,22 :button22 ,23 :button23 ,24 :button24 ,25 :button25 ,26 :button26 ,27 :button27 ,28 :button28 ,29 :button29 ,30 :button30 ,31 :button31 ,32 :button32 ,33 :button33 ,34 :button34 ,35 :button35 ,36 :button36 ,37 :button37 ,38 :button38 ,39 :button39 ,40 :button40 ,41 :button41 ,42 :button42 ,43 :button43 ,44 :button44 ,45 :button45 ,46 :button46 ,47 :button47 ,48 :button48 ,49 :button49 ,50 :button50 ,51 :button51 ,52 :button52 ,53 :button53 ,54 :button54 ,55 :button55 ,56 :button56 ,57 :button57 ,58 :button58 ,59 :button59 ,60 :button60 ,61 :button61 ,62 :button62 ,63 :button63 ,64 :button64}
    pos={button1:[0,1],button2:[0,2],button3:[0,3],button4:[0,4],button5:[0,5],button6:[0,6],button7:[0,7],button8:[0,8],button9:[1,1],button10:[1,2],button11:[1,3],button12:[1,4],button13:[1,5],button14:[1,6],button15:[1,7],button16:[1,8],button17:[2,1],button18:[2,2],button19:[2,3],button20:[2,4],button21:[2,5],button22:[2,6],button23:[2,7],button24:[2,8],button25:[3,1],button26:[3,2],button27:[3,3],button28:[3,4],button29:[3,5],button30:[3,6],button31:[3,7],button32:[3,8],button33:[4,1],button34:[4,2],button35:[4,3],button36:[4,4],button37:[4,5],button38:[4,6],button39:[4,7],button40:[4,8],button41:[5,1],button42:[5,2],button43:[5,3],button44:[5,4],button45:[5,5],button46:[5,6],button47:[5,7],button48:[5,8],button49:[6,1],button50:[6,2],button51:[6,3],button52:[6,4],button53:[6,5],button54:[6,6],button55:[6,7],button56:[6,8],button57:[7,1],button58:[7,2],button59:[7,3],button60:[7,4],button61:[7,5],button62:[7,6],button63:[7,7],button64:[7,8]}
    pos1={(0,1):button1,(0,2):button2,(0,3):button3,(0,4):button4,(0,5):button5,(0,6):button6,(0,7):button7,(0,8):button8,(1,1):button9,(1,2):button10,(1,3):button11,(1,4):button12,(1,5):button13,(1,6):button14,(1,7):button15,(1,8):button16,(2,1):button17,(2,2):button18,(2,3):button19,(2,4):button20,(2,5):button21,(2,6):button22,(2,7):button23,(2,8):button24,(3,1):button25,(3,2):button26,(3,3):button27,(3,4):button28,(3,5):button29,(3,6):button30,(3,7):button31,(3,8):button32,(4,1):button33,(4,2):button34,(4,3):button35,(4,4):button36,(4,5):button37,(4,6):button38,(4,7):button39,(4,8):button40,(5,1):button41,(5,2):button42,(5,3):button43,(5,4):button44,(5,5):button45,(5,6):button46,(5,7):button47,(5,8):button48,(6,1):button49,(6,2):button50,(6,3):button51,(6,4):button52,(6,5):button53,(6,6):button54,(6,7):button55,(6,8):button56,(7,1):button57,(7,2):button58,(7,3):button59,(7,4):button60,(7,5):button61,(7,6):button62,(7,7):button63,(7,8):button64}
    main.mainloop()
    time1=datetime.now()
    t=time1-time
    time=Tk()
    time.title('Game Timer')
    time.geometry('400x400+0+0')
    time.icon_set = Image("photo",file="clock.png")
    time.call('wm','iconphoto',main._w,time.icon_set)
    time.config(bg='black')
    showinfo('Time',str(t))
    if click==True:
        time.destroy()

main_fun()