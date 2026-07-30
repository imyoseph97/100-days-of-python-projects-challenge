import random

logo = r"""
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       """


print(logo)

the_number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempt = 0

if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5

while attempt != 0:
    print(f"You have {attempt} attempt remaining to guesss the number.")
    guess = int(input("Make a guess: "))
    if guess < the_number:
        print("Too low.")
        attempt -= 1
    elif guess > the_number:
        print("Too high")
        attempt -= 1
    else:
        print(f"You got it! The answer was {the_number}")
        break
else:
    print("You've run out of guesses. Refresh the page to run again.")

