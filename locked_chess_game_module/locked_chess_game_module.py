import json
import tkinter
import threading
import time
import sys
def game_start():
    global game
    global operation_number
    global operation_oppsite
    global operation_last_direction
    global all_operation
    global choose_chess_locate
    game={(8, 5, '白'), (5, 5, '黑'), (4, 4, '黑'), (9, 9, '黑'), (5, 8, '白'), (8, 8, '黑'), (9, 4, '白'), (4, 9, '白')}
    operation_number=1
    operation_oppsite='黑'
    operation_last_direction='无'
    all_operation=['u','d','l','r']
    choose_chess_locate='无'





def legal_operation():
    global all_operation
    global choose_chess_locate
    global operation_number
    global operation_oppsite
    global game
    class GameHasNotStartedError(Exception):
        pass
    class IllegalLocationError(Exception):
        pass
    def _check_game():    
        try:
            game
            operation_number
            operation_oppsite
            operation_last_direction
            choose_chess_locate
        except Exception:
            if __name__=='__main__':
                return ('001',"The game has not started yet .Please start the game with 'game_start()' .")
            else:
                return ('001',"The game has not started yet .Please start the game with 'example.game_start()' if you use 'import locked_chess_game_module as example' or 'game_start()' if you use 'from locked_chess_game_module import *' .")                      
        def legal_tuple(x:tuple):
            if len(x)!=3:
                if __name__=='__main__':
                    return ('002',"The length of the tuple '{}' in 'game' is wrong .".format(x))
                else:
                    return ('002',"The length of the tuple '{}' in 'example.game' if you use 'import locked_chess_game_module as example' or 'game' if you use 'from locked_chess_game_module import *' is wrong .".format(x))
            elif not (isinstance(x[0],int) and isinstance(x[1],int)):
                if __name__=='__main__':
                    return ('004',"The type of the first or second values in '{}' in 'game' are not all 'int' .".format(x))
                else:
                    return ('004',"The type of the first or second values in '{}' in 'example.game' if you use 'import locked_chess_game_module as example' or 'game' if you use 'from locked_chess_game_module import *' are not all 'int' .".format(x))
            elif not (1<=x[0]<=12 and 1<=x[1]<=12):
                return ('003',"Chess '{}' is not on the board .".format(x))
            elif x[2] not in ('黑','白'):
                return ('003',"Chess '{}' is unknown which oppsite it belongs to .".format(x))
            else:
                return ('000',)
        number_black=0
        number_white=0
        all_locate=[]
        if not isinstance(game,set):
            if __name__=='__main__':
                return ('004',"The type of 'game' is not 'set' .")
            else:
                return ('004',"The type of 'example.game' if you use 'import locked_chess_game_module as example' or 'game' if you use 'from locked_chess_game_module import *' is not 'set' .")
        for x in game:
            if not isinstance(x,tuple):
                if __name__=='__main__':
                    return ('004',"The type of '{}' in 'game' is not 'tuple' .".format(x))
                else:
                    return ('004',"The type of '{}' in 'example.game' if you use 'import locked_chess_game_module as example' or 'game' if you use 'from locked_chess_game_module import *' is not 'tuple' .".format(x))
            if (y:=legal_tuple(x))!=('000',):
                return y
            if (x[0],x[1]) in all_locate:
                return ('003',"Location '{}' has two or more chesses: '{}' .".format((x[0],x[1]),tuple([m for m in game if m[:-1]==(x[0],x[1])])))
            all_locate.append((x[0],x[1]))
            if x[2]=='黑':
                number_black+=1
            else:
                number_white+=1        
        if number_black<3 or number_white<3:
            return ('002',"The number of the chess is illegal .")
        if operation_number not in (1,2,3,4,5):
            if __name__=='__main__':
                return ('002',"The value of 'operation_number' should be in '(1,2,3,4,5)' .")
            else:
                return ('002',"The value of 'example.operation_number' if you use 'import locked_chess_game_module as example' or 'operation_number' if you use 'from locked_chess_game_module import *' should be in '(1,2,3,4,5)' .")
        if operation_oppsite not in ('黑','白'):
            if __name__=='__main__':
                return ('002',"The value of 'operation_oppsite' should be in '('黑','白')' .")
            else:
                return ('002',"The value of 'example.operation_oppsite' if you use 'import locked_chess_game_module as example' or 'operation_oppsite' if you use 'from locked_chess_game_module import *' should be in '('黑','白')' .")
        if operation_number in (2,5) and operation_last_direction not in ('上下','左右') or (operation_number in (1,3,4) and operation_last_direction!='无'):
            if __name__=='__main__':
                return ('002',"The value of 'operation_last_direction' is illegal .")
            else:
                return ('002',"The value of 'example.operation_last_direction' if you use 'import locked_chess_game_module as example' or 'operation_last_direction' if you use 'from locked_chess_game_module import *' is illegal .")    
        if operation_number in (4,5) and choose_chess_locate not in game or (operation_number in (1,2,3) and choose_chess_locate!='无'):
            if __name__=='__main__':
                return ('002',"The value of 'choose_chess_locate' is illegal .")
            else:
                return ('002',"The value of 'example.choose_chess_locate' if you use 'import locked_chess_game_module as example' or 'choose_chess_locate' if you use 'from locked_chess_game_module import *' is illegal .")
        else:
            return ('000',)
    all_operation=[]
    if (x:=_check_game())!=('000',):
        if x[0]=='001':
            m='raise GameHasNotStartedError(x[1])'            
            del all_operation            
            try:
                del choose_chess_locate
            except Exception:
                pass
            try:
                del operation_number
            except Exception:
                pass
            try:
                del operation_oppsite
            except Exception:
                pass
            try:
                del game
            except Exception:
                pass
            exec(m)
        elif x[0]=='002':
            m='raise ValueError(x[1])'
        elif x[0]=='003':
            m='raise IllegalLocationError(x[1])'
        else:
            m='raise TypeError(x[1])'
        del all_operation
        del choose_chess_locate
        del operation_number
        del operation_oppsite
        del game
        exec(m)    
    def legal_operation_all():
        bloa={'u':True,'d':True,'l':True,'r':True}
        wloa={'u':True,'d':True,'l':True,'r':True}
        for i in game:
            if i[-1]=='黑':
                if i[1]==1:
                    bloa['u']=False
                if i[1]==12:
                    bloa['d']=False
                if i[0]==1:
                    bloa['l']=False
                if i[0]==12:
                    bloa['r']=False
                if (i[0],i[1]-1,'白') in game:
                    bloa['u']=False
                    wloa['d']=False
                if (i[0],i[1]+1,'白') in game:
                    bloa['d']=False
                    wloa['u']=False
                if (i[0]-1,i[1],'白') in game:
                    bloa['l']=False
                    wloa['r']=False
                if (i[0]+1,i[1],'白') in game:
                    bloa['r']=False
                    wloa['l']=False
            else:
                if i[1]==1:
                    wloa['u']=False
                if i[1]==12:
                    wloa['d']=False
                if i[0]==1:
                    wloa['l']=False
                if i[0]==12:
                    wloa['r']=False
        return (bloa,wloa)
    def legal_operation_one():
        bloo={}
        wloo={}
        for i in game:
            if i[-1]=='黑':
                bloo[(i[0],i[1],'黑')]={'u':True,'d':True,'l':True,'r':True}
            else:
                wloo[(i[0],i[1],'白')]={'u':True,'d':True,'l':True,'r':True}
        for b in bloo.keys():
            if b[1]==1 or (b[0],b[1]-1,'黑') in game or (b[0],b[1]-1,'白') in game:
                bloo[b]['u']=False
            if b[1]==12 or (b[0],b[1]+1,'黑') in game or (b[0],b[1]+1,'白') in game:
                bloo[b]['d']=False
            if b[0]==1 or (b[0]-1,b[1],'黑') in game or (b[0]-1,b[1],'白') in game:
                bloo[b]['l']=False
            if b[0]==12 or (b[0]+1,b[1],'黑') in game or (b[0]+1,b[1],'白') in game:
                bloo[b]['r']=False
        for b in wloo.keys():
            if b[1]==1 or (b[0],b[1]-1,'黑') in game or (b[0],b[1]-1,'白') in game:
                wloo[b]['u']=False
            if b[1]==12 or (b[0],b[1]+1,'黑') in game or (b[0],b[1]+1,'白') in game:
                wloo[b]['d']=False
            if b[0]==1 or (b[0]-1,b[1],'黑') in game or (b[0]-1,b[1],'白') in game:
                wloo[b]['l']=False
            if b[0]==12 or (b[0]+1,b[1],'黑') in game or (b[0]+1,b[1],'白') in game:
                wloo[b]['r']=False
        return (bloo,wloo)
    direction_sort=['u','d','l','r']
    
    if operation_number in (1,2):
        if operation_oppsite=='黑':
            for i in legal_operation_all()[0].keys():
                if legal_operation_all()[0][i] \
                and (operation_number==1 or (operation_number==2 \
                and ((i in ('u','d') and operation_last_direction=='左右') \
                or (i in ('l','r') and operation_last_direction=='上下')))):
                    all_operation.append(i)
        else:
            for i in legal_operation_all()[1].keys():
                if legal_operation_all()[1][i] \
                and (operation_number==1 or (operation_number==2 \
                and ((i in ('u','d') and operation_last_direction=='左右') \
                or (i in ('l','r') and operation_last_direction=='上下')))):
                    all_operation.append(i)
        all_operation=sorted(all_operation,key=lambda x:direction_sort.index(x))
    elif operation_number in (4,5):        
        if operation_oppsite=='黑':
            for i in legal_operation_one()[0][choose_chess_locate].keys():
                if legal_operation_one()[0][choose_chess_locate][i] \
                and (operation_number==4 or (operation_number==5 \
                and ((i in ('u','d') and operation_last_direction=='左右') \
                or (i in ('l','r') and operation_last_direction=='上下')))):
                    all_operation.append(i)
        else:
            for i in legal_operation_one()[1][choose_chess_locate].keys():
                if legal_operation_one()[1][choose_chess_locate][i] \
                and (operation_number==4 or (operation_number==5 \
                and ((i in ('u','d') and operation_last_direction=='左右') \
                or (i in ('l','r') and operation_last_direction=='上下')))):
                    all_operation.append(i)
        all_operation=sorted(all_operation,key=lambda x:direction_sort.index(x))
    else:
        for i in game:
            if i[-1]==operation_oppsite:
                all_operation.append(i)
                all_operation.sort()
    if len(all_operation)==0:
        return 'fail'
    else:
        return all_operation


def operation(x):
    class IllegalOperationError(Exception):
        pass

    class GameFailError(Exception):
        pass
    global choose_chess_locate
    global operation_number
    global operation_oppsite
    global all_operation
    def change_game(a:int,b:int):
        global game
        global choose_chess_locate
        game_change=[]
        for i in game:
            game_change.append(list(i))
        game=set()
        for i_ in game_change:
            if operation_number in (1,2):
                if i_[-1]==operation_oppsite:
                    i_[a]+=b
            elif operation_number in (4,5):
                if (i_[0],i_[1])==choose_chess_locate[:-1]:
                    i_[a]+=b
            game.add(tuple(i_))
        if operation_number==4:
            choose_chess_locate=list(choose_chess_locate)
            choose_chess_locate[a]+=b
            choose_chess_locate=tuple(choose_chess_locate)

    def u():
        global operation_last_direction
        change_game(1,-1)
        if operation_number in (1,4):
            operation_last_direction='上下'
        else:
            operation_last_direction='无'

    def d():
        global operation_last_direction
        change_game(1,1)
        if operation_number in (1,4):
            operation_last_direction='上下'
        else:
            operation_last_direction='无'

    def l():
        global operation_last_direction
        change_game(0,-1)
        if operation_number in (1,4):
            operation_last_direction='左右'
        else:
            operation_last_direction='无'

    def r():
        global operation_last_direction
        change_game(0,1)
        if operation_number in (1,4):
            operation_last_direction='左右'
        else:
            operation_last_direction='无'
    gamestart=True
    legal_operation()
    if legal_operation()=='fail':
        if __name__=='__main__':
            a="The game is over ,and operatior '{}' has failed .Please start a new game with 'game_start()'".format(operation_oppsite)
            
        else:
            a="The game is over ,and operatior '{}' has failed .Please start a new game with 'example.game_start()' if you use 'import locked_chess_game_module as example' or 'game_start()' if you use 'from locked_chess_game_module import *'".format(operation_oppsite)
        GameFail="raise GameFailError(a)"    
        exec(GameFail)
    elif x in all_operation:
        if operation_number in (1,2,4,5):
            exec('{}()'.format(x))
        else:
            choose_chess_locate=x
        if operation_number!=5:
            operation_number+=1
        else:
            operation_number=1
            choose_chess_locate='无'
            if operation_oppsite=='黑':
                operation_oppsite='白'
            else:
                operation_oppsite='黑'
        legal_operation()
    else:
        if __name__=='__main__':
            a="Operation '{}' is not in list 'all_operation' .Please check your operation .".format(x)            
        else:
            a="Operation '{}' is not in list 'example.all_operation' if you use 'import locked_chess_game_module as example' or 'all_operation' if you use 'from locked_chess_game_module import *' .Please check your operation .".format(x)
        IllegalOperation="raise IllegalOperationError(a)"
        exec(IllegalOperation)
def return_game():    
    legal_operation()
    state=[[0 for i in range(12)] for i in range(12)]
    black_positions=[(i[1]-1,i[0]-1) for i in game if i[-1]=='黑']
    white_positions=[(i[1]-1,i[0]-1) for i in game if i[-1]=='白']
    for black in black_positions:
        state[black[0]][black[1]]=1
    for white in white_positions:
        state[white[0]][white[1]]=-1
    a={
            'all_locate':str(state),
            'operation_number':operation_number,
            'operation_oppsite':operation_oppsite,
            'operation_last_direction':operation_last_direction,
            'choose_chess_locate':str(choose_chess_locate),
            'all_operation':str(all_operation)
                }        

    return json.dumps(a,sort_keys=True)

def loads_game(x):
    global game
    global operation_number
    global operation_oppsite
    global operation_last_direction
    global choose_chess_locate
    legal_json=True
    无='无'
    try:
        all_information=json.loads(x)
        operation_number=all_information['operation_number']
        operation_oppsite=all_information['operation_oppsite']
        operation_last_direction=all_information['operation_last_direction']
        choose_chess_locate=eval(all_information['choose_chess_locate'])
        game=set()
    except Exception:
        try:
            del choose_chess_locate
        except Exception:
            pass
        try:
            del operation_number
        except Exception:
            pass
        try:
            del operation_oppsite
        except Exception:
            pass
        try:
            del game
        except Exception:
            pass
    else:
        if 'all_locate' not in all_information.keys() and 'game' not in all_information.keys():
            del all_operation
            del choose_chess_locate
            del operation_number
            del operation_oppsite
            del game
        elif 'all_locate' in all_information.keys() and 'game' in all_information.keys():
            del all_operation
            del choose_chess_locate
            del operation_number
            del operation_oppsite
            del game
        else:
            if 'all_locate' in all_information.keys():                
                try:
                    all_locate=eval(all_information['all_locate'])
                    for i1 in range(12):
                        for i2 in range(12):
                            if all_locate[i1][i2]==1:
                                game.add((i2+1,i1+1,'黑'))
                            elif all_locate[i1][i2]==-1:
                                game.add((i2+1,i1+1,'白'))
                            elif all_locate[i1][i2]==0:
                                pass
                            else:
                                del all_operation
                                del choose_chess_locate
                                del operation_number
                                del operation_oppsite
                                del game
                                raise Exception
                except Exception:
                    pass
            else:
                game=eval(all_information['game'])
    try:
        legal_operation()
    except Exception as e:
        legal_json=False
        error=e
    if not legal_json:
        m='raise ValueError("Wrong json : {}.")'.format(error)
        exec(m)
    
    
    
    
    
def main():    
    global game
    global operation_number
    global operation_oppsite
    global operation_last_direction
    global all_operation
    global choose_chess_locate
    operation_number=1
    locked_chess_tk=tkinter.Tk()
    locked_chess_tk.title('锁棋')
    locked_chess_tk.attributes('-fullscreen',True)
    locked_chess_tk.update()
    qipan=tkinter.Canvas(locked_chess_tk)
    hei=locked_chess_tk.winfo_height()*0.72
    qipan.place(relx=0.33,rely=0.1,width=hei,height=hei)
    h=locked_chess_tk.winfo_height()*0.7/520
    is_open=True
    tips=tkinter.Label(locked_chess_tk)
    tips.place(relx=0.8,rely=0.45)
    for i in range(13):                                    #创建棋盘
        qipan.create_line(40*h,40*(i+1)*h,520*h,40*(i+1)*h)
        qipan.create_line(40*(i+1)*h,40*h,40*(i+1)*h,520*h)
        if i!=0:
            qipan.create_text(20*h,(20+40*i)*h,text=str(i),font=('Arial',15),fill='green')
            qipan.create_text((20+40*i)*h,20*h,text=str(i),font=('Arial',15),fill='green')
    qi={'black':'黑','white':'白'}
    qi_read={}
    for xread in range(1,13):
        for yread in range(1,13):
            for zread in qi.keys():
                qi_read[qipan.create_oval((40*xread+5)*h,(40*yread+5)*h,(40*xread+35)*h,(40*yread+35)*h,fill=zread)]=(xread,yread,qi[zread])
    for id_read in qi_read.keys():
        qipan.itemconfig(id_read,state="hidden")

    def normal_chess():
        for i in qi_read.keys():
            if qi_read[i] in game:
                qipan.itemconfig(i,state="normal")
            else:
                qipan.itemconfig(i,state="hidden")
    all_game_information=tkinter.Label(locked_chess_tk)
    all_game_information.place(relx=0.03,rely=0.25)
    operation_translate={'u':'↑','d':'↓','l':'←','r':'→'}
    def get_recent_information():
        if all_operation:
            all_game_information.config(justify=tkinter.LEFT,text='全部黑棋坐标:{}\n全部白棋坐标:{}\n当前操作方:{}\n当前操作步数:{}\n上步全部可能操作(仅当前操作步数为2或5时显示，其它时候显示“无”):{}\n当前全部操作:{}\n当前选择棋子坐标(仅当前操作为4或5时显示，其它时候显示“无”):{}'.format(''.join([str((i[0],i[1])) for i in game if i[-1]=='黑']),''.join([str((i[0],i[1])) for i in game if i[-1]=='白']),operation_oppsite,operation_number,operation_last_direction,','.join([operation_translate[i] if operation_number!=3 else str((i[0],i[1])) for i in all_operation]),''.join([str((choose_chess_locate[0],choose_chess_locate[1])) if operation_number in (4,5) else '无'])))
        else:
            all_game_information.config(justify=tkinter.LEFT,text='全部黑棋坐标:{}\n全部白棋坐标:{}\n当前操作方:{}\n当前操作步数:{}\n上步全部可能操作(仅当前操作步数为2或5时显示，其它时候显示“无”):{}\n当前全部操作:{}\n当前选择棋子坐标(仅当前操作为4或5时显示，其它时候显示“无”):{}'.format(''.join([str((i[0],i[1])) for i in game if i[-1]=='黑']),''.join([str((i[0],i[1])) for i in game if i[-1]=='白']),operation_oppsite,operation_number,operation_last_direction,'{}方已经失败'.format(operation_oppsite),''.join([str((choose_chess_locate[0],choose_chess_locate[1])) if operation_number in (4,5) else '无'])))
    def start_game():
        a=operation_number                    
        game_start()
        normal_chess()
        get_recent_information()
        move.acquire()
        move.notify()
        move.release()
        if a==3:
            click.acquire()
            click.notify()
            click.release()
    move=threading.Condition()
    operation3=threading.Condition()
    click=threading.Condition()
    def has_clicked():
        click.acquire()
        click.notify()
        click.release()
    def clicked(event):
        nonlocal clicking
        clicking=0
        try:
            id_=event.widget.find_withtag('current')[0]
        except Exception:
            clicking=0
        else:
            clicking=id_
            if operation_number==3:
                has_clicked_true=threading.Thread(target=has_clicked)
                has_clicked_true.start()
    locked_chess_tk.bind('<Button-1>',clicked)
    clicking=0
    def up():
        operation('u')
        normal_chess()
        get_recent_information()
        be_up.configure(state=tkinter.DISABLED)
        be_down.configure(state=tkinter.DISABLED)
        be_left.configure(state=tkinter.DISABLED)
        be_right.configure(state=tkinter.DISABLED)
        move.acquire()
        move.notify()
        move.release()
    def down():
        operation('d')
        normal_chess()
        get_recent_information()
        be_up.configure(state=tkinter.DISABLED)
        be_down.configure(state=tkinter.DISABLED)
        be_left.configure(state=tkinter.DISABLED)
        be_right.configure(state=tkinter.DISABLED)
        move.acquire()
        move.notify()
        move.release()
    def left():
        operation('l')
        normal_chess()
        get_recent_information()
        be_up.configure(state=tkinter.DISABLED)
        be_down.configure(state=tkinter.DISABLED)
        be_left.configure(state=tkinter.DISABLED)
        be_right.configure(state=tkinter.DISABLED)
        move.acquire()
        move.notify()
        move.release()
    def right():
        operation('r')
        normal_chess()
        get_recent_information()
        be_up.configure(state=tkinter.DISABLED)
        be_down.configure(state=tkinter.DISABLED)
        be_left.configure(state=tkinter.DISABLED)
        be_right.configure(state=tkinter.DISABLED)
        move.acquire()
        move.notify()
        move.release()
    def legal_button():
        while is_open:
            move.acquire()
            move.wait()
            if not is_open:
                break            
            if legal_operation()!='fail':
                if operation_number!=3:                
                    if 'u' in legal_operation():
                        be_up.configure(state=tkinter.NORMAL)
                    else:
                        be_up.configure(state=tkinter.DISABLED)
                    if 'd' in legal_operation():
                        be_down.configure(state=tkinter.NORMAL)
                    else:
                        be_down.configure(state=tkinter.DISABLED)
                    if 'l' in legal_operation():
                        be_left.configure(state=tkinter.NORMAL)
                    else:
                        be_left.configure(state=tkinter.DISABLED)
                    if 'r' in legal_operation():
                        be_right.configure(state=tkinter.NORMAL)
                    else:
                        be_right.configure(state=tkinter.DISABLED)
                    if operation_number in (1,2):
                        tips.config(text="现在轮到{}棋全体移动".format(operation_oppsite))
                    if operation_number in (1,4,5):
                        if operation_number==5:
                            regreting.configure(state=tkinter.DISABLED)
                        try:
                            han.join()
                        except Exception:
                            pass
                        finally:
                            if operation_number!=1:
                                han=threading.Thread(target=hidden_and_normal)
                                han.start()
                else:
                    be_up.configure(state=tkinter.DISABLED)
                    be_down.configure(state=tkinter.DISABLED)
                    be_left.configure(state=tkinter.DISABLED)
                    be_right.configure(state=tkinter.DISABLED)
                    operation3.acquire()
                    operation3.notify()
                    operation3.release()
            else:
                be_up.configure(state=tkinter.DISABLED)
                be_down.configure(state=tkinter.DISABLED)
                be_left.configure(state=tkinter.DISABLED)
                be_right.configure(state=tkinter.DISABLED)
                if operation_oppsite=="黑":
                    tips.config(text="白方胜")
                else:
                    tips.config(text="黑方胜")
    def operation_3():
        global choose_chess_number
        global choose_chess_locate        
        nonlocal clicking
        while is_open:
            operation3.acquire()
            operation3.wait()
            if operation_number!=3 and is_open:
                continue
            if not is_open:
                break
            clicking=0
            choose_chess_locate='无'
            tips.config(text="请选择一个{}棋：".format(operation_oppsite))
            while choose_chess_locate[-1]!=operation_oppsite:                
                click.acquire()
                click.wait()
                if operation_number!=3 or not is_open:
                    break
                if clicking in qi_read.keys():
                    if qi_read[clicking][-1]==operation_oppsite:
                        choose_chess_number=clicking
                        operation(qi_read[clicking])
                    else:
                        tips.config(text="未选择{}棋，请重新选择：".format(operation_oppsite))
            else:
                tips.config(text="选择完成，请移动这枚{}棋。\n在移动前可点击“撤回”撤回选择".format(operation_oppsite))
                regreting.configure(state=tkinter.NORMAL)
                get_recent_information()
                move.acquire()
                move.notify()
                move.release()    
    def be_regret():
        global operation_number
        global choose_chess_locate
        if operation_number==4:
            operation_number-=1
            for i in qi_read.keys():
                if qi_read[i]==choose_chess_locate:
                    qipan.itemconfig(i,state="normal")
                    break
            choose_chess_locate='无'
            legal_operation()
            get_recent_information()
            regreting.configure(state=tkinter.DISABLED)
            be_up.configure(state=tkinter.DISABLED)
            be_down.configure(state=tkinter.DISABLED)
            be_left.configure(state=tkinter.DISABLED)
            be_right.configure(state=tkinter.DISABLED)
            operation3.acquire()
            operation3.notify()
            operation3.release()
    def hidden_and_normal():
        m=operation_number
        while m==operation_number:
            for i in qi_read.keys():
                if qi_read[i]==choose_chess_locate:
                    qipan.itemconfig(i,state="hidden")
                    time.sleep(0.5)
                    if m!=operation_number:
                        break                    
                    normal_chess()
                    time.sleep(0.5)
                
    
    regreting=tkinter.Button(locked_chess_tk,text="撤回",command=be_regret)
    regreting.place(relx=0.84,rely=0.35)
    regreting.configure(state=tkinter.DISABLED)
    be_up=tkinter.Button(locked_chess_tk,text="   ↑   ",command=up)
    be_up.place(relx=0.8,rely=0.7)
    be_down=tkinter.Button(locked_chess_tk,text="   ↓   ",command=down)
    be_down.place(relx=0.8,rely=0.75)
    be_left=tkinter.Button(locked_chess_tk,text="   ←   ",command=left)
    be_left.place(relx=0.76,rely=0.75)
    be_right=tkinter.Button(locked_chess_tk,text="   →   ",command=right)
    be_right.place(relx=0.835,rely=0.75)
    be_up.configure(state=tkinter.DISABLED)
    be_down.configure(state=tkinter.DISABLED)
    be_left.configure(state=tkinter.DISABLED)
    be_right.configure(state=tkinter.DISABLED)
    show_legal_button=threading.Thread(target=legal_button,daemon=True)
    show_legal_button.start()
    operation_is_3=threading.Thread(target=operation_3,daemon=True)
    operation_is_3.start()
    def rule_known():
        rule=tkinter.Tk()
        rule.geometry("500x250")
        rules=tkinter.Label(rule)
        rule.title('规则')
        rules.config(text="""黑先，双方轮流移动棋子，每轮分以下步骤：\n1.选择一个方向移动全部棋子一格。\n2.选择一个与上一个方向垂直的方向移动全部棋子一格。\n3.选择己方一个棋子。\n4.选择一个方向移动选择的棋子一格。\n5.选择一个与上一个方向垂直的方向移动选择的棋子一格。\n移动时棋子不能出界，不能碰到其它棋子。\n当一方无法移动棋子时另一方获胜。\n\n本游戏规则由黄皓华一人独立发现。""")
        name_indicate=tkinter.Label(rule,text='▲▲▲',fg='red')
        name_indicate.place(relx=0.24,rely=0.78)        
        rules.config(justify=tkinter.LEFT)
        rules.place(relx=0.1,rely=0.1)
    rule_want_to_know=tkinter.Button(locked_chess_tk,text="规则",command=rule_known)
    rule_want_to_know.place(relx=0.1,rely=0.5)
    be_beginning=tkinter.Button(locked_chess_tk,text="开始",command=start_game)
    be_beginning.place(relx=0.15,rely=0.5)
    def go_back():
        nonlocal is_open
        locked_chess_tk.destroy()
        is_open=False        
        sys.exit(0)                
    back=tkinter.Button(locked_chess_tk,text="退出",command=go_back)
    back.place(relx=0.2,rely=0.5)
    locked_chess_tk.mainloop()

if __name__=='__main__':
    main()
