Below are the global variables that locked_chess_game_module.py defined:
	game --all of the chesses'location and belonging
	operation_number --the number of steps taken by the current operation
	operation_oppsite --who is currently operating
	operation_last_direction --previous possible actions . If operation_number is 1 , 3 or 4 , it's value is '无'
	choose_chess_locate --which chess is being chosen now . If operation_number is 1 , 2 or 3 ,it's value is '无'
	all_operation --all of the operations that comply with the rule

Below are the functions that locked_chess_game_module.py defined:
	game_start() --start a new game
	legal_operation() --return all_operation . If there is no operation that comply with the rule , return 'fail' . (Warning : if the variables do not all conform to the rule , this function will delete all of the variables above and raise an Exception . It means that you need to start a new game .)
	operation(x) --do the operation 'x' . If 'x' is not in all_operation or the game is over , it will raise an Exception .
	return_game() --return a json string that describes the game statement .
	loads_game(x) --translate the json string 'x' . (Warning : If 'x' does not compile the rule , it will raise an Exception and delete all of the global variables . It means that you need to start a new game .)

Below is the rule of the variables:
	1 . Variable 'game' must be a set , and what is in the set must be a tuple whose length is 3 .
	2 . The tuples above must be (int_1,int_2,'黑') or (int_1,int_2,'白') . The int_1 and int_2 should between 1 to 12 (contain 1 and 12) . The number of the tuples whose last element is '黑' and those whose last element is '白' should be greater than or equal to 3 . Different tuples shouldn't have the same int_1 and same int_2 at the same time .
	3 . 'operation_oppsite' can only be '黑' or '白' .
	4 . 'operation_number' can only be 1 , 2 , 3 , 4 or 5 .
	5 . If operation_number is 2 or 5 , variable 'operation_last_direction' can only be '上下' or '左右' . Else variable 'operation_last_direction' can only be '无' .
	6 . If operation_number is 4 or 5 , variable 'choose_chess_locate' can only be a tuple in set 'game' .Else variable 'choose_chess_locate' can only be '无' .

Below is the rule of the json:
	1 . Should contain 'operation_number' , 'operation_oppsite' , 'operation_last_direction' , 'choose_chess_locate' .
	2 . Should contain 'all_locate' or 'game' , but shouldn't contain all of them .
	3 . 'all_locate' should be a string directly converted from a list which contains 12 lists which contain 12 numbers -1 , 0 or 1 . The other should be a string directly converted from the variables above .

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
		① . Choose a direction from 'up' , 'down' , 'left' , 'right' to move all of the operater's chesses . 
		② . Choose a direction that perpendicular to the last direction chosen to move all of the operater's chesses . 
		③ . Choose one operater's  chess .
		④ . Choose a direction from 'up' , 'down' , 'left' , 'right' to move the chosen chess .
		⑤ . Choose a direction that perpendicular to the last direction chosen to move the chosen chess .
	3 . When moving , the chesses shouldn't be moved to the other chesses'position or be out of the board .
	4 . When the operater now can't take any operations , the other win .