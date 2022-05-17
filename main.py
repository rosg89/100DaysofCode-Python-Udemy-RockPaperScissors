import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose?\n0.Rock\n1.Paper\n2.Scissors\n"))

if user_choice >= 3 or user_choice <0:
  print("You typed an invalid number, you lose!")
else:
  print(f"You choose option {user_choice}\n{game_images[user_choice]}")
  computer_choice = random.randint(0,2)
  print(f"The computer chose {computer_choice}\n{game_images[computer_choice]}")
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif user_choice >= 3 or user_choice <0:
    print("Yoy typed an invalid number, you lose!")
  elif computer_choice > user_choice:
    print("You lose!")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("Draw!")
