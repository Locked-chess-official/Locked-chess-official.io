import json
import tkinter
import sys
import threading
import time
import ast

class LockedChessClass:
    def __init__(self):
        self.game_start()
    
    def game_start(self):
        self.game={(8, 5, '白'), (5, 5, '黑'), (4, 4, '黑'), (9, 9, '黑'), (5, 8, '白'), (8, 8, '黑'), (9, 4, '白'), (4, 9, '白')}
        self.operation_number=1
        self.operation_oppsite='黑'
        self.operation_last_direction='无'
        self.all_operation=['u','d','l','r']
        self.choose_chess_locate='无'

    def legal_operation(self):
        class GameHasNotStartedError(Exception):
            pass
        class IllegalLocationError(Exception):
            pass
        def check_game(self):    
            try:
                self.game
                self.operation_number
                self.operation_oppsite
                self.operation_last_direction
                self.choose_chess_locate
            except Exception:                
                return ('001',"The game has not started yet .Please start the game with 'game_start()' .")                
            def legal_tuple(x:tuple):
                if len(x)!=3:
                    return ('002',f"The length of the tuple '{x}' in 'game' is wrong .")
                elif not (isinstance(x[0],int) and isinstance(x[1],int)):
                    return ('004',f"The type of the first or second values in '{x}' in 'game' are not all 'int' .")                    
                elif not (1<=x[0]<=12 and 1<=x[1]<=12):
                    return ('003',f"Chess '{x}' is not on the board .")
                elif x[2] not in ('黑','白'):
                    return ('003',f"Chess '{x}' is unknown which oppsite it belongs to .")
                else:
                    return ('000',)
            number_black=0
            number_white=0
            all_locate=[]
            if not isinstance(self.game,set):                
                return ('004',"The type of 'game' is not 'set' .")
            for x in self.game:
                if not isinstance(x,tuple):                    
                    return ('004',f"The type of '{x}' in 'game' is not 'tuple' .")                    
                if (y:=legal_tuple(x))!=('000',):
                    return y
                if (x[0],x[1]) in all_locate:
                    return ('003',f"Location '{(x[0],x[1])}' has two or more chesses: '{tuple([m for m in game if m[:-1]==(x[0],x[1])])}' .")
                all_locate.append((x[0],x[1]))
                if x[2]=='黑':
                    number_black+=1
                else:
                    number_white+=1        
            if number_black<3 or number_white<3:
                return ('002',"The number of the chess is illegal .")
            if self.operation_number not in (1,2,3,4,5):
                return ('002',"The value of 'operation_number' should be in '(1,2,3,4,5)' .")
            if self.operation_oppsite not in ('黑','白'):
                return ('002',"The value of 'operation_oppsite' should be in '('黑','白')' .")
            if (self.operation_number in (2,5) and \
               self.operation_last_direction not in ('上下','左右')) or \
               (self.operation_number in (1,3,4) and \
                self.operation_last_direction!='无'):                
                return ('002',"The value of 'operation_last_direction' is illegal .") 
            if (self.operation_number in (4,5) and \
               self.choose_chess_locate not in self.game) or \
               (self.operation_number in (1,2,3) and \
                self.choose_chess_locate!='无'):
                return ('002',"The value of 'choose_chess_locate' is illegal .")                
            else:
                return ('000',)
            
        self.all_operation=[]
        if (x:=check_game(self))!=('000',):
            if x[0]=='001':
                m='raise GameHasNotStartedError(x[1])'            
                del self.all_operation            
                try:
                    del self.choose_chess_locate
                except Exception:
                    pass
                try:
                    del self.operation_number
                except Exception:
                    pass
                try:
                    del self.operation_oppsite
                except Exception:
                    pass
                try:
                    del self.game
                except Exception:
                    pass
                exec(m)
            elif x[0]=='002':
                m='raise ValueError(x[1])'
            elif x[0]=='003':
                m='raise IllegalLocationError(x[1])'
            else:
                m='raise TypeError(x[1])'
            del self.all_operation
            del self.choose_chess_locate
            del self.operation_number
            del self.operation_oppsite
            del self.game
            exec(m)
            
        def legal_operation_all(self):
            bloa={'u':True,'d':True,'l':True,'r':True}
            wloa={'u':True,'d':True,'l':True,'r':True}
            for i in self.game:
                if i[-1]=='黑':
                    if i[1]==1:
                        bloa['u']=False
                    if i[1]==12:
                        bloa['d']=False
                    if i[0]==1:
                        bloa['l']=False
                    if i[0]==12:
                        bloa['r']=False
                    if (i[0],i[1]-1,'白') in self.game:
                        bloa['u']=False
                        wloa['d']=False
                    if (i[0],i[1]+1,'白') in self.game:
                        bloa['d']=False
                        wloa['u']=False
                    if (i[0]-1,i[1],'白') in self.game:
                        bloa['l']=False
                        wloa['r']=False
                    if (i[0]+1,i[1],'白') in self.game:
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
        
        def legal_operation_one(self):
            bloo={}
            wloo={}
            for i in self.game:
                if i[-1]=='黑':
                    bloo[(i[0],i[1],'黑')]={'u':True,'d':True,'l':True,'r':True}
                else:
                    wloo[(i[0],i[1],'白')]={'u':True,'d':True,'l':True,'r':True}
            for b in bloo.keys():
                if b[1]==1 or (b[0],b[1]-1,'黑') in self.game or (b[0],b[1]-1,'白') in self.game:
                    bloo[b]['u']=False
                if b[1]==12 or (b[0],b[1]+1,'黑') in self.game or (b[0],b[1]+1,'白') in self.game:
                    bloo[b]['d']=False
                if b[0]==1 or (b[0]-1,b[1],'黑') in self.game or (b[0]-1,b[1],'白') in self.game:
                    bloo[b]['l']=False
                if b[0]==12 or (b[0]+1,b[1],'黑') in self.game or (b[0]+1,b[1],'白') in self.game:
                    bloo[b]['r']=False
            for b in wloo.keys():
                if b[1]==1 or (b[0],b[1]-1,'黑') in self.game or (b[0],b[1]-1,'白') in self.game:
                    wloo[b]['u']=False
                if b[1]==12 or (b[0],b[1]+1,'黑') in self.game or (b[0],b[1]+1,'白') in self.game:
                    wloo[b]['d']=False
                if b[0]==1 or (b[0]-1,b[1],'黑') in self.game or (b[0]-1,b[1],'白') in self.game:
                    wloo[b]['l']=False
                if b[0]==12 or (b[0]+1,b[1],'黑') in self.game or (b[0]+1,b[1],'白') in self.game:
                    wloo[b]['r']=False
            return (bloo,wloo)
        
        direction_sort=['u','d','l','r']        
        if self.operation_number in (1,2):
            if self.operation_oppsite=='黑':
                for i in legal_operation_all(self)[0].keys():
                    if legal_operation_all(self)[0][i] \
                    and (self.operation_number==1 or (self.operation_number==2 \
                    and ((i in ('u','d') and self.operation_last_direction=='左右') \
                    or (i in ('l','r') and self.operation_last_direction=='上下')))):
                        self.all_operation.append(i)
            else:
                for i in legal_operation_all(self)[1].keys():
                    if legal_operation_all(self)[1][i] \
                    and (self.operation_number==1 or (self.operation_number==2 \
                    and ((i in ('u','d') and self.operation_last_direction=='左右') \
                    or (i in ('l','r') and self.operation_last_direction=='上下')))):
                        self.all_operation.append(i)
            self.all_operation=sorted(self.all_operation,key=lambda x:direction_sort.index(x))
        elif self.operation_number in (4,5):        
            if self.operation_oppsite=='黑':
                for i in legal_operation_one(self)[0][self.choose_chess_locate].keys():
                    if legal_operation_one(self)[0][self.choose_chess_locate][i] \
                    and (self.operation_number==4 or (self.operation_number==5 \
                    and ((i in ('u','d') and self.operation_last_direction=='左右') \
                    or (i in ('l','r') and self.operation_last_direction=='上下')))):
                        self.all_operation.append(i)
            else:
                for i in legal_operation_one(self)[1][self.choose_chess_locate].keys():
                    if legal_operation_one(self)[1][self.choose_chess_locate][i] \
                    and (self.operation_number==4 or (self.operation_number==5 \
                    and ((i in ('u','d') and self.operation_last_direction=='左右') \
                    or (i in ('l','r') and self.operation_last_direction=='上下')))):
                        self.all_operation.append(i)
            self.all_operation=sorted(self.all_operation,key=lambda x:direction_sort.index(x))
        else:
            for i in self.game:
                if i[-1]==self.operation_oppsite:
                    self.all_operation.append(i)
                    self.all_operation.sort()
        if len(self.all_operation)==0:
            return 'fail'
        else:
            return self.all_operation


    def operation(self,x):
        class IllegalOperationError(Exception):
            pass

        class GameIsOverError(Exception):
            pass
        
        def change_game(self,a:int,b:int):
            game_change=[]
            for i in self.game:
                game_change.append(list(i))
            self.game=set()
            for i_ in game_change:
                if self.operation_number in (1,2):
                    if i_[-1]==self.operation_oppsite:
                        i_[a]+=b
                elif self.operation_number in (4,5):
                    if (i_[0],i_[1])==self.choose_chess_locate[:-1]:
                        i_[a]+=b
                self.game.add(tuple(i_))
            if self.operation_number==4:
                self.choose_chess_locate=list(self.choose_chess_locate)
                self.choose_chess_locate[a]+=b
                self.choose_chess_locate=tuple(self.choose_chess_locate)

        def u(self):
            change_game(self,1,-1)
            if self.operation_number in (1,4):
                self.operation_last_direction='上下'
            else:
                self.operation_last_direction='无'

        def d(self):
            change_game(self,1,1)
            if self.operation_number in (1,4):
                self.operation_last_direction='上下'
            else:
                self.operation_last_direction='无'

        def l(self):
            change_game(self,0,-1)
            if self.operation_number in (1,4):
                self.operation_last_direction='左右'
            else:
                self.operation_last_direction='无'

        def r(self):
            change_game(self,0,1)
            if self.operation_number in (1,4):
                self.operation_last_direction='左右'
            else:
                self.operation_last_direction='无'
                
        self.legal_operation()
        if self.legal_operation()=='fail':            
            a=f"The game is over ,and operatior '{self.operation_oppsite}' has failed .Please start a new game with 'game_start()'"                          
            gamefail="raise GameIsOverError(a)"    
            exec(gamefail)
        elif x in self.all_operation:
            if self.operation_number in (1,2,4,5):
                exec(f'{x}(self)')
            else:
                self.choose_chess_locate=x
            if self.operation_number!=5:
                self.operation_number+=1
            else:
                self.operation_number=1
                self.choose_chess_locate='无'
                if self.operation_oppsite=='黑':
                    self.operation_oppsite='白'
                else:
                    self.operation_oppsite='黑'
            self.legal_operation()
        else:            
            a=f"Operation '{x}' is not in list 'all_operation' .Please check your operation ."                 
            illegaloperation="raise IllegalOperationError(a)"
            exec(illegaloperation)

    def return_game(self):    
        self.legal_operation()
        state=[[0 for i in range(12)] for i in range(12)]
        black_positions=[(i[1]-1,i[0]-1) for i in self.game if i[-1]=='黑']
        white_positions=[(i[1]-1,i[0]-1) for i in self.game if i[-1]=='白']
        for black in black_positions:
            state[black[0]][black[1]]=1
        for white in white_positions:
            state[white[0]][white[1]]=-1
        a={
                'all_locate':str(state),
                'operation_number':self.operation_number,
                'operation_oppsite':self.operation_oppsite,
                'operation_last_direction':self.operation_last_direction,
                'choose_chess_locate':str(self.choose_chess_locate),
                'all_operation':str(self.all_operation)
                    }        
        return json.dumps(a,sort_keys=True)

    def loads_game(self,x):
        legal_json=True
        error1='operation_number ,operation_oppsite ,operation_last_direction ,choose_chess_locate are all exist and legal.'
        error2=''
        try:
            all_information=json.loads(x)
            self.operation_number=all_information['operation_number']
            self.operation_oppsite=all_information['operation_oppsite']
            self.operation_last_direction=all_information['operation_last_direction']
            if all_information['choose_chess_locate']!='无':
                self.choose_chess_locate=ast.literal_eval(all_information['choose_chess_locate'])
            else:
                self.choose_chess_locate='无'
            self.game=set()
        except Exception as e1:
            error1=f'operation_number ,operation_oppsite ,operation_last_direction ,choose_chess_locate are not all exist and legal :{str(e1)}.'
            try:
                del self.choose_chess_locate
            except Exception:
                pass
            try:
                del self.operation_number
            except Exception:
                pass
            try:
                del self.operation_oppsite
            except Exception:
                pass
            try:
                del self.game
            except Exception:
                pass
        else:            
            if 'all_locate' not in all_information.keys() and 'game' not in all_information.keys():
                error2="both key 'all_locate' and 'game' are not exist .It is illegal ."
                del self.all_operation
                del self.choose_chess_locate
                del self.operation_number
                del self.operation_oppsite
                del self.game
            elif 'all_locate' in all_information.keys() and 'game' in all_information.keys():
                error2="both key 'all_locate' and 'game' are exist .It is illegal ."
                del self.all_operation
                del self.choose_chess_locate
                del self.operation_number
                del self.operation_oppsite
                del self.game
            else:
                error2="only one key 'all_locate' and 'game' is exist .It is legal ."
                if 'all_locate' in all_information.keys():                
                    try:
                        if len(all_locate:=ast.literal_eval(all_information['all_locate']))!=12:
                            raise Exception("length of key's value's eval whose name is  'all_locate' should be 12 .")
                        for i1 in range(12):
                            if len(all_locate[i1])!=12:
                                raise Exception("length of values in key's value's eval whose name is  'all_locate' should be 12 .")
                            for i2 in range(12):
                                if all_locate[i1][i2]==1:
                                    self.game.add((i2+1,i1+1,'黑'))
                                elif all_locate[i1][i2]==-1:
                                    self.game.add((i2+1,i1+1,'白'))
                                elif all_locate[i1][i2]==0:
                                    pass
                                else:
                                    raise Exception("values in key's value's eval whose name is  'all_locate' should be only in (-1,0,1)")
                    except Exception as e2:
                        error2+='but {}'.format(str(e2))
                        del self.all_operation
                        del self.choose_chess_locate
                        del self.operation_number
                        del self.operation_oppsite
                        del self.game
                else:
                    try:
                        self.game=ast.literal_eval(all_information['game'])
                    except Exception as e2:
                        error2+='but {}'.format(str(e2))
                        del self.all_operation
                        del self.choose_chess_locate
                        del self.operation_number
                        del self.operation_oppsite
                        del self.game
        try:
            self.legal_operation()
        except Exception as e:
            legal_json=False
            error=error1+' '+error2+' '+str(e)
        if not legal_json:
            m=f'''raise ValueError("Wrong json .{"'"+error+"'"} Please check your input . ")'''
            exec(m)

def main():
    def normal_chess():
        for i in qi_read.keys():
            if qi_read[i] in locked_chess_game_.game:
                qipan.itemconfig(i,state="normal")
            else:
                qipan.itemconfig(i,state="hidden")
                
    def get_recent_information():
        if locked_chess_game_.all_operation:
            all_game_information.config(justify=tkinter.LEFT,
                                        text=f'''全部黑棋坐标:{''.join([str((i[0],i[1])) for i in locked_chess_game_.game if i[-1]=='黑'])}
全部白棋坐标:{''.join([str((i[0],i[1])) for i in locked_chess_game_.game if i[-1]=='白'])}
当前操作方:{locked_chess_game_.operation_oppsite}
当前操作步数:{locked_chess_game_.operation_number}
上步全部可能操作(仅当前操作步数为2或5时显示，其它时候显示“无”):{locked_chess_game_.operation_last_direction}
当前全部操作:{','.join([operation_translate[i] if locked_chess_game_.operation_number!=3 else str((i[0],i[1])) for i in locked_chess_game_.all_operation])}
当前选择棋子坐标(仅当前操作为4或5时显示，其它时候显示“无”):{''.join([str((locked_chess_game_.choose_chess_locate[0],locked_chess_game_.choose_chess_locate[1])) if locked_chess_game_.operation_number in (4,5) else '无'])}'''
                                        )
        else:
            all_game_information.config(justify=tkinter.LEFT,
                                        text=f'''全部黑棋坐标:{''.join([str((i[0],i[1])) for i in locked_chess_game_.game if i[-1]=='黑'])}
全部白棋坐标:{''.join([str((i[0],i[1])) for i in locked_chess_game_.game if i[-1]=='白'])}
当前操作方:{locked_chess_game_.operation_oppsite}
当前操作步数:{locked_chess_game_.operation_number}
上步全部可能操作(仅当前操作步数为2或5时显示，其它时候显示“无”):{locked_chess_game_.operation_last_direction}
当前全部操作:{locked_chess_game_.operation_oppsite}方已经失败
当前选择棋子坐标(仅当前操作为4或5时显示，其它时候显示“无”):{''.join([str((locked_chess_game_.choose_chess_locate[0],locked_chess_game_.choose_chess_locate[1])) if locked_chess_game_.operation_number in (4,5) else '无'])}'''
                                        )

    def start_game():
        a=locked_chess_game_.operation_number
        locked_chess_game_.game_start()
        normal_chess()
        get_recent_information()
        move.acquire()
        move.notify()
        move.release()
        if a==3:
            click.acquire()
            click.notify()
            click.release()
    
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
            if locked_chess_game_.operation_number==3:
                has_clicked_true=threading.Thread(target=has_clicked)
                has_clicked_true.start()
                
    def up():
        locked_chess_game_.operation('u')
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
        locked_chess_game_.operation('d')
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
        locked_chess_game_.operation('l')
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
        locked_chess_game_.operation('r')
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
            if locked_chess_game_.legal_operation()!='fail':
                if locked_chess_game_.operation_number!=3:                
                    if 'u' in locked_chess_game_.all_operation:
                        be_up.configure(state=tkinter.NORMAL)
                    else:
                        be_up.configure(state=tkinter.DISABLED)
                    if 'd' in locked_chess_game_.all_operation:
                        be_down.configure(state=tkinter.NORMAL)
                    else:
                        be_down.configure(state=tkinter.DISABLED)
                    if 'l' in locked_chess_game_.all_operation:
                        be_left.configure(state=tkinter.NORMAL)
                    else:
                        be_left.configure(state=tkinter.DISABLED)
                    if 'r' in locked_chess_game_.all_operation:
                        be_right.configure(state=tkinter.NORMAL)
                    else:
                        be_right.configure(state=tkinter.DISABLED)
                    if locked_chess_game_.operation_number in (1,2):
                        tips.config(text=f"现在轮到{locked_chess_game_.operation_oppsite}棋全体移动")
                    if locked_chess_game_.operation_number in (1,4,5):
                        if locked_chess_game_.operation_number==5:
                            regreting.configure(state=tkinter.DISABLED)
                        try:
                            han.join()
                            del han
                        except Exception:
                            pass
                        finally:
                            if locked_chess_game_.operation_number!=1:
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
                if locked_chess_game_.operation_oppsite=="黑":
                    tips.config(text="白方胜")
                else:
                    tips.config(text="黑方胜")
                    
    def operation_3():
        nonlocal choose_chess_number
        nonlocal clicking
        while is_open:
            operation3.acquire()
            operation3.wait()
            if locked_chess_game_.operation_number!=3 and is_open:
                continue
            if not is_open:
                break
            clicking=0
            locked_chess_game_.choose_chess_locate='无'
            tips.config(text=f"请选择一个{locked_chess_game_.operation_oppsite}棋：")
            while locked_chess_game_.choose_chess_locate[-1]!=locked_chess_game_.operation_oppsite:                
                click.acquire()
                click.wait()
                if locked_chess_game_.operation_number!=3 or not is_open:
                    break
                if clicking in qi_read.keys():
                    if qi_read[clicking][-1]==locked_chess_game_.operation_oppsite:
                        choose_chess_number=clicking
                        locked_chess_game_.operation(qi_read[clicking])
                    else:
                        tips.config(text=f"未选择{locked_chess_game_.operation_oppsite}棋，请重新选择：")
            else:
                tips.config(text=f"选择完成，请移动这枚{locked_chess_game_.operation_oppsite}棋。\n在移动前可点击“撤回”撤回选择")
                regreting.configure(state=tkinter.NORMAL)
                get_recent_information()
                move.acquire()
                move.notify()
                move.release()

    def be_regret():
        nonlocal choose_chess_number
        if locked_chess_game_.operation_number==4:
            locked_chess_game_.operation_number-=1
            for i in qi_read.keys():
                if qi_read[i]==locked_chess_game_.choose_chess_locate:
                    qipan.itemconfig(i,state="normal")
                    break
            locked_chess_game_.choose_chess_locate='无'
            locked_chess_game_.legal_operation()
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
        m=locked_chess_game_.operation_number
        while m==locked_chess_game_.operation_number:
            for i in qi_read.keys():
                if qi_read[i]==locked_chess_game_.choose_chess_locate:
                    qipan.itemconfig(i,state="hidden")
                    time.sleep(0.5)
                    if m!=locked_chess_game_.operation_number:
                        break                    
                    normal_chess()
                    time.sleep(0.5)

    def rule_known():
        rule=tkinter.Tk()
        rule.geometry("500x250")
        rules=tkinter.Label(rule)
        rule.title('规则')
        rules.config(justify=tkinter.LEFT,text="""黑先，双方轮流移动棋子，每轮分以下步骤：
1.选择一个方向移动全部棋子一格。
2.选择一个与上一个方向垂直的方向移动全部棋子一格。
3.选择己方一个棋子。
4.选择一个方向移动选择的棋子一格。
5.选择一个与上一个方向垂直的方向移动选择的棋子一格。
移动时棋子不能出界，不能碰到其它棋子。
当一方无法移动棋子时另一方获胜。
\n本游戏规则由黄皓华一人独立发现。""")
        name_indicate=tkinter.Label(rule,text='▲▲▲',fg='red')
        name_indicate.place(relx=0.24,rely=0.78)        
        rules.place(relx=0.1,rely=0.1)
        
    def go_back():
        nonlocal is_open
        locked_chess_tk.destroy()
        is_open=False        
        sys.exit(0)
        
    locked_chess_game_=LockedChessClass()
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
    for i in range(13): 
        qipan.create_line(40*h,40*(i+1)*h,520*h,40*(i+1)*h)
        qipan.create_line(40*(i+1)*h,40*h,40*(i+1)*h,520*h)
        if i!=0:
            qipan.create_text(20*h,(20+40*i)*h,text=str(i),font=('Arial',15),fill='green')
            qipan.create_text((20+40*i)*h,20*h,text=str(i),font=('Arial',15),fill='green')
    all_game_information=tkinter.Label(locked_chess_tk)
    all_game_information.place(relx=0.03,rely=0.25)
    operation_translate={'u':'↑','d':'↓','l':'←','r':'→'}
    qi={'black':'黑','white':'白'}
    qi_read={}
    for xread in range(1,13):
        for yread in range(1,13):
            for zread in qi.keys():
                qi_read[qipan.create_oval((40*xread+5)*h,(40*yread+5)*h,(40*xread+35)*h,(40*yread+35)*h,fill=zread)]=(xread,yread,qi[zread])        
    for id_read in qi_read.keys():
        qipan.itemconfig(id_read, state="hidden")
    move=threading.Condition()
    operation3=threading.Condition()
    click=threading.Condition()
    locked_chess_tk.bind('<Button-1>',clicked)
    clicking=0    
    choose_chess_number=0    
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
    rule_want_to_know=tkinter.Button(locked_chess_tk,text="规则",command=rule_known)
    rule_want_to_know.place(relx=0.1,rely=0.5)
    be_beginning=tkinter.Button(locked_chess_tk,text="开始",command=start_game)
    be_beginning.place(relx=0.15,rely=0.5)
    back=tkinter.Button(locked_chess_tk,text="退出",command=go_back)
    back.place(relx=0.2,rely=0.5)
    locked_chess_tk.mainloop()

if __name__=='__main__':
    main()
