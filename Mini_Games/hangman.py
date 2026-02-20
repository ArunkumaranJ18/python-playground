import random

intro = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
'''

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


print("Welcome to Hangman!")
word_list = ["laptop", "mouse", "keyboard"]

chosen_word = random.choice(word_list)
guessed_word = []
final_result = ""

for i in range(0,len(chosen_word)):
    guessed_word.append("_")

game_over = False
number_of_guesses = 0

print(intro)
print("Guess Word:" + "".join(guessed_word))

while(not game_over) :
    print(f"************************************{6 - number_of_guesses}/6 **************************************")
    guessed_letter = input("Please guess a letter: ").lower()
    guess_result = False
    if guessed_letter in final_result:
        print("You already guessed this letter!")
    for i in range(0,len(chosen_word)):
        if guessed_letter == chosen_word[i]:
            guessed_word[i] = guessed_letter
            guess_result = True
            final_result = "".join(guessed_word)
            print(final_result)


    if(not guess_result and number_of_guesses <= 6) :
        number_of_guesses += 1
        print(HANGMANPICS[number_of_guesses])

    if(final_result == chosen_word):
        print("You win!")
        game_over = True

    if(number_of_guesses >= 6):
        print("You lose!")
        game_over = True