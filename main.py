"""
Bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie

autor: Jaroslav Hoferek
email: jaroslav.hoferek@seznam.cz
discord: Jaroslav H. | Mazurel#7763
"""

# PART 0: Import modules and greeting player.
# Import random module for random generating.

import random

separator = "-" * 60

print(f"{separator}\nHello there!!!\n{separator}\n\
I have generated random four-digits number, let´s beggin!!!\n{separator}")

# PART 1: Generating guessed number.
# Def. new function "random_number". 
# This function contains list of numbers for random generating purposes,
# and return random four-digits list.

def random_number() -> list:
    numbers = [1, 2, 3, 4, 5, 6, 7, 9]
    return random.sample(numbers, 4)

# Def. new function for connecting numbers in list.

def secret(random_list: list) -> str:
    number = [str(i) for i in random_list]
    result = ("".join(number))
    return str(result)

# PART 2: Player move verification.
# First create variable "game" for while loop and 
# variable "attemps" for countin attemps.
# First "while" loop.
# This loop checks if game is still running (game == True).
#   Second "while" loop.
#   This loop controls player input till auxiliary variable "number" == False.
#       ask for player input number
#       in every iteration attempts += 1.
#       if number entered by player is not digit -> print attention and number == False.
#       elif if number entered by player contains more or less than 4 digits -> print attention and number == False.
#       elif if number entered by player starts by 0 -> print attention and number == False.
#       elif if number entered by player contains a recurring character -> print attention and number == False.
#       else:
#           number = True
print(secret(mystery_number))
game = True
attempts = 0
while game != False:
    number = False
    while number != True:
        player_move = input("Enter the number:\n")
        attempts +=1
        if player_move.isdigit() != True:
            number = False
            print("A bad character was entered, try it again!")
        elif len(player_move) < 4 or len(player_move) > 4:
            number = False
            print("The number must be four-digit, try it again!")
        elif player_move < "1000":
            number = False
            print("The number cannot start with zero, try it again!")
        elif len(set(player_move)) != 4:
            number = False
            print("Character in the number must be unique, try it again!")
        else:
            number = True
        
# PART 3: Turn evaluation.
# Create two variables for cows and bulls counting.
# In first "if" loop.
# if player_move == secret(mystery_number):
#   add +1 to attempts.
#   game = False
#   player win -> print notification with number of attempts and bulls.
# In "for" loop.
# for character in ramge of lengh secret(mystery_number):
#   if character in secret(mystery_number) is in player_move 
#   without matching position -> cows += 1.
#   elif character in secret(mystery_number) and
#   position is matching -> bulls += 1

    cows = 0
    bulls = 0
    
    if player_move == secret(mystery_number):
        game = False
    for character in range(len(secret(mystery_number))):
        if secret(mystery_number)[character] in player_move and secret(mystery_number)[character] != player_move[character]:
            cows += 1
        elif secret(mystery_number)[character] == player_move[character]:
            bulls += 1
# PART 4: Answer for player.
# Create two new variables for string purposes
# if value bulls variable != 1 -> print bulls in asnwer.
# else -> print bull in asnwer.
# if value cows variable != 1 -> print cows in asnwer.
# else -> print cow in asnwer.
# After every not winning turn -> print number of bulls/cows.
    bull = ""
    cow = ""

    if bulls == 1:
        bull = "bull."
    elif bulls == 4:
        bull = ("bulls, " + "you won for the " + str(attempts) + " attempts!")
    else:
        bull = "bulls."
    if cows == 1:
        cow = "cow"
    else:
        cow = "cows"

    print(f"{separator}\nThere is {cows} {cow} and {bulls} {bull}\n{separator}")
