import os
import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           """


cards  = [2,3,4,5,6,7,8,9,10,10,10,10,11]






play_again = True

def clear_screen():
    os.system("cls")


def the_game():
    print(logo)
    player = random.sample(cards, k = 2)
    dealer = random.choice(cards)
    while play_again:

        print(f"\tYour cards: {player}, current score: {sum(player)}")
        print(f"\tComputer's first card: {dealer}")

        picker = input("Type 'y' to get another card, 'n' to pass: ")

        if picker == 'y':
            x = random.choice(cards)
            if x == 11 and sum(player) + x > 21:
                x = 1
                player.append(x)
            elif 11 in player and sum(player) + x > 21:
                i = player.index(11)
                player[i] = 1
            else:
                player.append(x)  

            if sum(player) > 21:
                print(f"\tYour final hand: {player}. final score: {sum(player)}")
                print(f"\tComputer's final hand: {dealer}, final score: {dealer}")
                print(f"You went over. You lose 😭")
                break
            
        elif picker == 'n':
            dealer = [dealer]
            while sum(dealer) < 21:
                dealer.append(random.choice(cards))
            
            print(f"\tYour final hand: {player}. final score: {sum(player)}")
            print(f"\tComputer's final hand: {dealer}, final score: {sum(dealer)}")    
            if sum(dealer) > 21 and sum(player) <= 21:
                print("Opponent went over. You win 😁")
                break
            elif sum(dealer) == sum(player):
                print("Draw 🙃")
                break
            elif sum(dealer) == 21:
                print("Lose, opponent has Blackjack 😱")
                break
            
            elif sum(dealer) > sum(player) and sum(dealer) < 21 :
                print("You win 😃")
                break
            



while True:
    the_game()
    again = input("Do you want to play a game of BlackjacK? Type 'y' or 'n': ")
    if again == 'n':
        break
    elif again == 'y':
        clear_screen()

        
    





        


