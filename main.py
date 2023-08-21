"""
Bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie

autor: Jaroslav Hoferek
email: jaroslav.hoferek@seznam.cz
discord: Jaroslav H. | Mazurel#7763
"""

# PART 1.
import random

separator = "-" * 60

print(f"{separator}\nHello there!!!\n{separator}\n\
I have generated random four-digits number, let´s beggin!!!\n{separator}")

def random_list_generating() -> list:
    """
    Generates a random four-digit list 
    that does not start with zero.
    """
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    stop = True
    while stop == True:
        random_list = random.sample(numbers, 4)
        if random_list[0] == 0:
            random_list.pop(random_list[0])
        elif len(random_list) == 4:
            stop = False
    return random_list

def secret(random_list: list) -> str:
    """Convert list to string"""
    number = [str(i) for i in random_list]
    result = ("".join(number))
    return str(result)

mystery_number = secret(random_list_generating())

# PART 2.
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
        
# PART 3.
    cows = 0
    bulls = 0
    
    if player_move == mystery_number:
        game = False
    for character in range(len(mystery_number)):
        if mystery_number[character] in player_move and mystery_number[character] != player_move[character]:
            cows += 1
        elif mystery_number[character] == player_move[character]:
            bulls += 1

# PART 4.
    bull = ""
    cow = ""
    are_or_is = ""
    attempt = ""

    if attempts == 1:
        attempt = "attempt"
    else:
        attempt = "attempts"
    if bulls == 1:
        bull = "bull."
    elif bulls == 4:
        bull = ("bulls, " + "you won for the " + str(attempts) + f" {attempt}!")
    else:
        bull = "bulls."
    if cows == 1:
        cow = "cow"
        are_or_is = "is"
    else:
        cow = "cows"
        are_or_is = "are"

    print(f"{separator}\nThere {are_or_is} {cows} {cow} and {bulls} {bull}\n{separator}")
