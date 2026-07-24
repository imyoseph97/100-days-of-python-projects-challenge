import random

RPS = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

,"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

computer_chose = random.randint(0,2)

user_chose = int(input("What do you choose? Type 0 for Rcok, 1 for Paper or 2 for scissors.\n"))
if user_chose is 0 or 1 or 2:
    print(RPS[user_chose])
else:
    print("Please enter a valid number")

print("Computer chose:")

print(RPS[computer_chose])
if computer_chose == 1 and computer_chose == 0:
    print("You lose")
elif computer_chose == 2 and computer_chose == 0:
    print("You win")
elif computer_chose == 2 and computer_chose == 1:
    print("You lose")
elif computer_chose == 0 and user_chose == 1:
    print("You win")
elif computer_chose == 0 and user_chose == 2:
    print("You lose")
elif computer_chose == 1 and user_chose == 2:
    print("You win")
else:
    print("It's a draw")
     





    




