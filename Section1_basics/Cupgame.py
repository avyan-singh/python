import random
from random import shuffle

my_list=["","O",""]
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

my_list=shuffle_list(my_list)
def player_guess():
    guess=""
    print(my_list)
    guess=input("pick a number from 0 1 or 2:")
    while guess not in ["0","1","2"]:
        guess=input("pick a number from 0 1 or 2:")
    return int(guess)

def check_guess():
    guess=player_guess()
    if my_list[guess]=="O":
        print("correct guess!!")
    else:
        print("Wrong guess!!")
    

check_guess()
