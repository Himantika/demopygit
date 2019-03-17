from random import randint
from time import sleep

def user_guess():
    guess = int(input("Enter your guess: "))
    return guess

def dice_roll(sides_no):
    first_roll = randint(1, sides_no)
    second_roll = randint(1, sides_no)
    max_no = sides_no * 2
    total_no = first_roll + second_roll
    print("The maximum value you could select is; %d" % (max_no))
    guess = user_guess()
    if guess > max_no:
        print("You cannot exceed beyond the specified value")
    else:
        print("Rolling.....")
        sleep(2)
        print("The first roll is: %d" % (first_roll))
        sleep(2)
        print("The second roll is: %d" % (second_roll))
        sleep(2)
        print("The sum of both rolls is: %d" % (total_no))
        print("Result...")
        sleep(3)

        if guess >= total_no:
            print("Congrats! You win")
        else:
            print("Sorry! You Loose.")

dice_roll(6)
