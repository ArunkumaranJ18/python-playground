import random

stone = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [stone, paper, scissors]
stone_paper_scissors = ["Stone", "Paper", "Scissor"]
rand = random.randint(0,2)

print("Welcome to the Stone Paper Scissor Game!")
user_input = int(input("Please select 0 for stone or 1 for paper or 2 for scissor: "))

if user_input >= 0 and user_input <= 2:
    print(game_images[user_input])
    print("Computer chooses: ")
    print(game_images[rand])

if user_input < 0 or user_input > 2:
    print("Please select a valid option!")
elif user_input == rand:
    print("Draw the match!")
elif user_input == 0 and rand == 2:
    print(f"{stone_paper_scissors[user_input]} beats {stone_paper_scissors[rand]}, You win!")
elif user_input == 1 and rand == 0:
    print(f"{stone_paper_scissors[user_input]} beats {stone_paper_scissors[rand]}, You win!")
elif user_input == 2 and rand == 1:
    print(f"{stone_paper_scissors[user_input]} beats {stone_paper_scissors[rand]}, You win!")
else:
    print(f"{stone_paper_scissors[rand]} beats {stone_paper_scissors[user_input]}, You lose!")
