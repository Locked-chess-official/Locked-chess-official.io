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
    这意味着你向集合game添加了第一个或第二个元素类型不都是整数的元组
</pre>
