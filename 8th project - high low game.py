logo = '''

   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   




'''
print(logo)

import random

continue_game = True

while continue_game:
    ans = input("Would you like to play a game of High Low?"
                " Please type 'y' for yes or 'n' for no. ")
    if ans == "n":
        continue_game = False
    elif ans == "y":
        target_number = random.randint(1, 100)
        print("\nWelcome to the High Low game\n"
              "Im thinking of a number between 1 and 100."
              " Can you guess what it is?  ")
        print(f"cheat code, the answer is {target_number}")
        right_input = False
        while not right_input:
            difficulty = input("\nPlease choose a difficulty, type in 'easy' or 'hard'. ")
            if difficulty == "easy":
                lives = 10
                right_input = True
            elif difficulty == "hard":
                lives = 5
                right_input = True
            else:
                print("Type in 'easy' or 'hard'. ")


        end_of_game = False
        while not end_of_game:
            if lives == 0:
                print("You ran out of lives. \n")
                end_of_game = True
                break
            print(f"You have {lives} attempts remaining to guess the number. ")
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 100:
                print("\nPlease enter a number between 1 and 100. \n")
            elif guess == target_number:
                print(f"You got it, the answer was {target_number}. \n")
                end_of_game = True
            elif guess > target_number:
                print("Too high. \n")
                lives -= 1
            elif guess < target_number:
                print("Too low. \n")
                lives -= 1
        else:
            print("Please type 'y' for yes or 'n' for no. ")
