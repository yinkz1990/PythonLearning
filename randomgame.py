import sys
import time
from random import randint

sys.argv

# Initial Steps to invite in the game:
print("\nWelcome to Guess game by Idumu\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Random!")
time.sleep(3)


def guess_game():
    global number
    global random_number
    number = int(input('Kindly guess a number between 1 and 10: '))
    random_number = randint(1, 10)


def thegame():
    guess_game()
    count = 0
    while True:
        try:
            if count < 10:
                if number == random_number:
                    print(
                        f'Great work!!!! \n The number is thesame with the random number \n The number of Trail is {count}')
                    break
                else:
                    count += 1
                    print('please try again')
                    guess_game()
            else:
                print(f'The game is over, your trail = {count}')
                break
        except (ValueError, TypeError) as err:
            print(err)


thegame()
