import random

logo = """    
 ,----.                                      ,--.  ,--.                                          ,--.                  
'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     ,--,--, ,--.,--.,--,--,--.|  |-.  ,---. ,--.--. 
|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  || .-. :    |      \|  ||  ||        || .-. '| .-. :|  .--' 
'  '--'  |'  ''  '\   --..-'  `).-'  `)      |  |  |  | |  |\   --.    |  ||  |'  ''  '|  |  |  || `-' |\   --.|  |    
 `------'  `----'  `----'`----' `----'       `--'  `--' `--' `----'    `--''--' `----' `--`--`--' `---'  `----'`--'
 """

def guess_the_number():

    print(logo)

    print("Welcome to the Number Guessing Game")

    print("I'm thinking of a number between 1 and 100")

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    lives = 0

    if difficulty_level == 'easy':
        lives = 10
    elif difficulty_level == 'hard':
        lives = 5
    else:
        print("The entered difficulty level is invalid.")
        return

    random_number = random.randint(1, 100)

    while lives > 0:
        print(f"You have {lives} attempts to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == random_number:
            print(f"You got it! The number is {random_number}.")
            return
        elif guess > random_number:
            print("Too high.")
        else:
            print("Too low.")
        lives -= 1

    print(f"The guessed number was {random_number}.")
    print("You've ran out of guesses, you lose.")

guess_the_number()