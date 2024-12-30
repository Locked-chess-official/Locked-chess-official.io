<pre>
Below is all of the exceptions you can see and defined by locked_chess_game_module.py .
以下是locked_chess_game_module.py定义的异常解释
  legal_operation():
  
    `GameHasNotStartedError:The game has not started yet .Please start the game with 'game_start()' .`
    `GameHasNotStartedError:The game has not started yet .Please start the game with 'example.game_start()' if you use 'import locked_chess_game_module as example' or 'game_start()' if you use 'from locked_chess_game_module import *' .`
 
    It means that the game's necessary global variables do not all exist .
    这意味着一些重要的游戏全局变量没有定义。
    
    `ValueError:The length of the tuple (e,x,a,m,p,l,e) in 'game' is wrong .`
    `ValueError:The length of the tuple (e,x,a,m,p,l,e) in 'example.game' if you use 'import locked_chess_game_module as example' or 'game' if you use 'from locked_chess_game_module import *' is wrong .`

    It means that you add a tuple whose length is not 3 to the set "game" .
    这意味着你向集合game中添加了长度不等于3的元组。

    `TypeError:The type of the first or second values in (e,x,a,m,p,l,e) in 'game' are not all 'int' .`
    `TypeError:The type of the first or second values in (e,x,a,m,p,l,e) in 'example.game' if you use 'import locked_chess_game_module as example' or 'game' if you use 'from locked_chess_game_module import *' are not all 'int' .`

    It means that you add a tuple whose first element and second element types are not all int to the set "game" .
    这意味着你向集合game添加了第一个与第二个元素类型不都是整数的元组。

    `IllegalLocationError:Chess (e,x,a,m,p,l,e) is not on the board .`

    It means that you add a tuple whose first element and second element types are not all between 1 and 12(contain 1,12) to the set "game" , which mean a chess piece's coordinates .
    这意味着你向集合game添加了第一个与第二个元素不都大于等于1且小于等于12的元组。它们代表棋子的坐标。

    `IllegalLocationError:Chess (e,x,a,m,p,l,e) is unknown which oppsite it belongs to .`

    It means that you add a tuple whose last element is not in ('黑','白') ， which means the oppsite which the chess piece belongs to .
    这意味着你向集合game添加了最后一个元素不是“黑”或“白”的元素。它代表棋子所属方。

    `TypeError:The type of 'game' is not 'set' .`
    `TypeError:The type of 'example.game' if you use 'import locked_chess_game_module as example' or 'game' if you use 'from locked_chess_game_module import *' is not 'set' .`

    It means that you assign a value whose type is not "set" to the variable "game" .
    这意味着你给变量game定义了一个不是集合的值。

    `TypeError:The type of 'example' in 'game' is not 'tuple' .`
    `TypeError:The type of 'example' in 'example.game' if you use 'import locked_chess_game_module as example' or 'game' if you use 'from locked_chess_game_module import *' is not 'tuple' .`

    It means that you add a things whose type is not "tuple" to the set "game" .
    这意味着你给集合game添加了不是元组的值。

    `IllegalLocationError:Location '(e,x,a,m,p,l,e)' has two or more chesses: '(example1,example2,…)' .`

    It means that tuple "example1","example2" and so on have the same first element and second element ， which means that two or more chesses are in the same position .
    这意味这后面元组具有相同的第一个与第二个元素，说明都在棋盘相同位置。

    `ValueError:The number of the chess is illegal .`

    It means that the number of the tuple whose last element is "黑" and the number of the tuple whose last element is "白" are not all equal or greater to 3 .
    这意味着最后一个元素为“黑”的元组数量与最后一个元素为“白”的元组数量不都大于等于3。

    `ValueError:The value of 'operation_number' should be in '(1,2,3,4,5)' .`
    `ValueError:The value of 'example.operation_number' if you use 'import locked_chess_game_module as example' or 'operation_number' if you use 'from locked_chess_game_module import *' should be in '(1,2,3,4,5)' .`

    It means that you assign a value which is not in (1,2,3,4,5) to the variable "operation_number" .
    这意味着你给变量operation_number赋予了一个不在1，2，3，4，5中的值

    `ValueError:The value of 'operation_oppsite' should be in '('黑','白')' .`
    `ValueError:The value of 'example.operation_oppsite' if you use 'import locked_chess_game_module as example' or 'operation_oppsite' if you use 'from locked_chess_game_module import *' should be in '('黑','白')' .`

    It means that you assign a value which is not in ('黑','白') to the variable "operation_oppsite" .
    这意味着你给变量operation_oppsite赋予了不是“黑”或“白”的值。
    
    `ValueError:The value of 'operation_last_direction' is illegal .`
    `ValueError:The value of 'example.operation_last_direction' if you use 'import locked_chess_game_module as example' or 'operation_last_direction' if you use 'from locked_chess_game_module import *' is illegal .`

    It means that you assign a value which is not in ("上下","左右") if operation_number in (2,5) or not "无" else to the variable "operation_last_direction" .
    这意味着你给变量operation_last_direction在operation_number为2或5时赋予了不为“上下”或“左右”的值或在其它情况下赋予了不为“无”的值。

    `ValueError:The value of 'choose_chess_locate' is illegal .`
    `ValueError:The value of 'example.choose_chess_locate' if you use 'import locked_chess_game_module as example' or 'choose_chess_locate' if you use 'from locked_chess_game_module import *' is illegal .`

    It means that you assign a value which is not in set "game" if operation_number in (4,5) or not "无" else to the variable "operation_last_direction" .
    这意味着你给变量operation_last_direction在operation_number为4或5时赋予了不为集合game中元素的值或在其它情况下赋予了不为“无”的值。

  operation(x):     --You maybe see the Exception above because this function needs to call "legal_operation()" . 
                    --你可能看到上面的异常因为该函数需要使用legal_operation()。

    `IllegalOperationError:Operation 'example' is not in list 'all_operation' .Please check your operation .`
    `IllegalOperationError:Operation 'example' is not in list 'example.all_operation' if you use 'import locked_chess_game_module as example' or 'all_operation' if you use 'from locked_chess_game_module import *' .Please check your operation .`

    It means that you are trying to take an operation which is not in the list "all_operation" . It can only take the operation which is in the list "all_operation" .
    这意味着你正在尝试进行一个列表all_operation中没有的操作。这个函数只能执行在列表all_operation中的操作。

    `GameFailedError:The game is over ,and operatior 'example' has failed .Please start a new game with 'game_start()' .`
    `GameFailedError:The game is over ,and operatior 'example' has failed .Please start a new game with 'example.game_start()' if you use 'import locked_chess_game_module as example' or 'game_start()' if you use 'from locked_chess_game_module import *' .`

    It means that now there is no operation you can take (you failed). You can only start a new game .
    这意味着目前你没有操作（你已经失败了）。你只能开始一个新的操作。

  loads_game():
    `ValueError:Wrong json . 'example_sentence.' Please check your input . `

    The "example_sentence" is in the Exception in "legal_operation()" . It can help you to current the mistake in the json .
    其中“example_sentence”是在legal_operation()中的报错，可以帮你改正json中的错误。
    
  
</pre>
