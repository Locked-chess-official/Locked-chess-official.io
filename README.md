<pre style="white-space: pre-wrap;max-width: 80ch;">
Below are the global variables that locked_chess_game_module.py defined:
	game --all of the chesses'location and belonging
	operation_number --the number of steps taken by the current operation
	operation_oppsite --who is currently operating
	operation_last_direction --previous possible actions . If operation_number is 1 , 3 or 4 , it's value is '无'
	choose_chess_locate --which chess is being chosen now . If operation_number is 1 , 2 or 3 ,it's value is '无'
	all_operation --all of the operations that comply with the rule

以下是locked_chess_game_module.py定义的全局变量：
	game --所有黑棋与白棋位置
	operation_number --当前操作进行到的步数
	operation_oppsite --当前操作方
	operation_last_direction --上一步可能的操作。如果operation的值为1、3或者4，这个变量的值为“无”
	choose_chess_locate --当前选择的棋子。若operation_number的值为1、2或者3，这个变量的值为“无“
	all_operation --当前全部符合规则的操作
	
Below are the functions that locked_chess_game_module.py defined:
	game_start() --start a new game
	legal_operation() --return all_operation . If there is no operation that comply with the rule , return 'fail' . 
	(Warning : if the variables do not all conform to the rule , this function will delete all of the variables above and raise an Exception . It means that you need to start a new game .)
	operation(x) --do the operation 'x' . If 'x' is not in all_operation or the game is over , it will raise an Exception .
	return_game() --return a json string that describes the game statement .
	loads_game(x) --translate the json string 'x' . 
	(Warning : If 'x' does not compile the rule , it will raise an Exception and delete all of the global variables . It means that you need to start a new game .)
	main() --a function that use 'tkinter' to play this game .

以下是locked_chess_game_module.py定义的函数：
	game_start() --开始新的一局。
	legal_operation() --生成并返回all_operation。若没有符合规则的操作，返回“fail”。
	(警告：若存在变量不符合规则，该函数将删除全部上述全局变量并报错，这意味着你要开始新的一盘。)
	operation(x) --进行操作x。如果操作x不在all_operation中或游戏已经结束，该函数将报错。
	return_game() --返回一个json字符串，该字符串描述当前棋局。
	loads_game(x) --将json字符串x翻译为棋局信息。
	(警告：若x不符合规范，这个函数将删除全部上述全局变量并报错，这意味着你要开始新的一盘。)
	main() --通过tkinter开始这个游戏。
	
Below is the rule of the variables:
	1 . Variable 'game' must be a set , and what is in the set must be a tuple whose length is 3 .
	2 . The tuples above must be (int_1,int_2,'黑') or (int_1,int_2,'白') . 
		①The int_1 and int_2 should between 1 to 12 (contain 1 and 12) . 
		②The number of the tuples whose last element is '黑' and those whose last element is '白' should be greater than or equal to 3 . 
		③Different tuples shouldn't have the same int_1 and same int_2 at the same time .
	3 . 'operation_oppsite' can only be '黑' or '白' .
	4 . 'operation_number' can only be 1 , 2 , 3 , 4 or 5 .
	5 . If operation_number is 2 or 5 , variable 'operation_last_direction' can only be '上下' or '左右' . Else variable 'operation_last_direction' can only be '无' .
	6 . If operation_number is 4 or 5 , variable 'choose_chess_locate' can only be a tuple in set 'game' .Else variable 'choose_chess_locate' can only be '无' .

以下是全局变量规范：
	1 变量”game”必须是集合，元素必须是长度为3的元组。
	2 元组必须是(整数1，整数2，”黑”)或(整数1，整数2，“白”)。
        	①整数1与整数2必须大于等于1且小于等于12。
		②最后一个元素为”黑”的元组与最后一个元素为“白”的元组数量都必须大于等于3。
		③任意两个元组不能同时拥有相同的整数1与整数2。
	3 “operation_oppsite”的值只能是“黑”或“白”。
	4 “operation_number”的值只能是1，2，3，4，5。
	5 当“operation_number”的值为2或5时，“operation_last_direction”的值只能是“上下”或“左右”。其它情况则只能为“无”。
	6 当“operation_number”的值为4或5时，“choose_chess_locate”的值必须是集合“game”中的元组。其它情况则只能为“无”。
	
Below is the rule of the json:
	1 . Should contain 'operation_number' , 'operation_oppsite' , 'operation_last_direction' , 'choose_chess_locate' .
	2 . Should contain 'all_locate' or 'game' , but shouldn't contain all of them .
	3 . 'all_locate' should be a string directly converted from a list which contains 12 lists which contain 12 numbers -1 , 0 or 1 . 
	4 . The other should be a string directly converted from the variables above . Check that they are confirm the rule .

以下是json字符串规范：
	1 必须包含键“operation_number”，“operation_oppsite”，“operation_last_direction”，“choose_chess_locate”。
	2 必须包含键“all_locate”或者“game”，但不能同时包含。
	3 键“all_locate”的值必须是一个由列表直接转变的字符串，该列表包含12个列表，每个列表包含12个数字，这些数字只能是0，1，-1
	4 其它键的值为对应变量变成的字符串，注意这些变量必须符合规范。

Below is the rule of the game 'locked chess' :
	1 . It is the beginning of the game :
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- --  ● -- -- -- -- ○ -- -- --
		-- -- -- --  ● -- -- ○ -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- --  ○ -- -- ● -- -- -- --
		-- -- --  ○ -- -- -- -- ● -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
	2 . Black first . Two player take turns , and each operation should be divided into the following 5 steps :
		① . Choose a direction from 'up' , 'down' , 'left' , 'right' to move all of the operater's chesses one square . 
		② . Choose a direction that perpendicular to the last direction chosen to move all of the operater's chesses one square . 
		③ . Choose one operater's  chess .
		④ . Choose a direction from 'up' , 'down' , 'left' , 'right' to move the chosen chess one square .
		⑤ . Choose a direction that perpendicular to the last direction chosen to move the chosen chess one square .
	3 . When moving , the chesses shouldn't be moved to the other chesses'position or be out of the board .
	4 . When the operater now can't take any operations , the other win .

以下是游戏“锁棋”的规则：
	1 以下为游戏默认初始局面：
	        -- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- --  ● -- -- -- -- ○ -- -- --
		-- -- -- --  ● -- -- ○ -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- --  ○ -- -- ● -- -- -- --
		-- -- --  ○ -- -- -- -- ● -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
		-- -- -- -- -- -- -- -- -- -- -- --
	2 黑棋先行，双方轮流操作，每次操作分5步完成：
        	① 从“上”、“下”、“左”、“右”中选择一个方向移动全部棋子一格。
	        ② 选择一个与上一步选择方向相垂直的方向移动全部棋子一格。
	        ③ 选择当前操作者的一个棋子。
	        ④ 从“上”、"下"、“左”、“右”中选择一个方向移动选择的棋子一格。
	        ⑤ 选择一个与上一步选择方向相垂直的方向移动选择的棋子一格。
	3 移动时棋子不能移动到其它棋子所在格或出界。
	4 当前操作者如果不能进行任何操作，另一方获胜。
	
How to use?
Move the folder to 'path\to\your\python\python3\Lib\site-packages' . Be sure that the version of the python is above 3.8 .

如何使用？
把文件夹移动到'path\to\your\python\python3\Lib\site-packages'中，注意确保python版本在3.8以上。
</pre>
