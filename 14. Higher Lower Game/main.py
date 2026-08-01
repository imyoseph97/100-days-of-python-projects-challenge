from Game_Data import data
import art
import random
import os


def clear_screen():
    os.system("cls")

is_correct = True


score = 0
while is_correct:
    
    A = random.choice(data)
    B = random.choice(data)
    a_count = A['follower_count']
    b_count = B['follower_count']

    if score == 0:
        print(art.logo)


    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    ask = input("Who has more followers? Type 'A' or 'B':").upper()
    
    
    winner = ''
    if a_count == b_count:
        B = random.choice(data)
    if a_count > b_count:
        winner = 'A'
    elif a_count < b_count:
        winner = 'B'
    

    if ask == winner:
        clear_screen()
        score += 1
        print(art.logo)
        print(f"You're right! Current Score: {score}")

    else:
        clear_screen()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break



        


