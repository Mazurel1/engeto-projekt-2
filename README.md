# engeto-projekt-2
### Game description
Bulls and Cows is a game where player guess random secret number \
which does not start with zero. Every turn player type his guess to console \
and get respond containing  numbers of cows and bulls (if some are there), \
which helps him to guess right number.

Cow = number is in secret number but does not match with right position. \
Bull = number is in secret number and match with right position.

### Brief code structure
Whole code could be split to four parts and in this section I will try explain main purpose each of them. \
It means there will not be explain mean every variable, loop or whatever else in depth.

Part 1: In this part are defined two functions which purpose is to generate secret number. \
First function generates random four-digit list of unique numbers and two conditions inside \
ensure that the first character of the list will not be zero. \
Second function converts list to string. In code is first function used as input for second. \
The result is four digit string of random numbers which does not star with zero.

Part 2: In this part is assessed player´s input against several conditions which are: \
-> The input entered by player can contain only numbers. \
-> The input must be four-digit long. \
-> The input must contain only unique numbers. \
If player corupt any of this conditions, then will be alerted which of these it was. \
This will continue until valid input will be entered.

Part 3: A player´s guess evaluation. The player´s turn evaluation is based on two 
cinditions. \
-> If player´s guess contain number which is in secret number but does not \
	match with right postition, player get a cow. 
 	Player gets one cow for each number which meet of this condition. \
-> If player´s guess contain number which is in secret number and match with right postition,\
	player get a bull. Player gets one bull for each number which meet of this condition.

Part 4: This part is responsible for announcing the results of the player's turn.
