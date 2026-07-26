import random


print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

lives = ['''          
  +---+
  |   |
      |
      |
      |
      |
=========
****************************6/6 LIVES LEFT****************************''','''  

  +---+
  |   |
  O   |
      |
      |
      |
=========
****************************5/6 LIVES LEFT****************************''', ''' 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========
****************************4/6 LIVES LEFT****************************''','''  

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
****************************3/6 LIVES LEFT****************************''', ''' 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
****************************2/6 LIVES LEFT****************************''', '''  

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
****************************1/6 LIVES LEFT****************************''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
****************************0/6 LIVES LEFT****************************''']




word_list = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "apricot", "blackberry", "blueberry", "cantaloupe", "cranberry", "currant", "gooseberry", "grapefruit", "guava",
    "lime", "lychee", "mandarin", "mulberry", "olive", "passionfruit", "peach", "pear", "persimmon", "plum",
    "pomegranate", "pomelo", "rhubarb", "starfruit", "aubergine", "broccoli", "cabbage", "carrot", "cauliflower", "celery",
    "corn", "cucumber", "eggplant", "garlic", "ginger", "lettuce", "mushroom", "onion", "pepper", "potato",
    "pumpkin", "radish", "spinach", "tomato", "turnip", "zucchini", "basil", "chives", "coriander", "dill",
    "mint", "oregano", "parsley", "rosemary", "sage", "thyme", "almond", "cashew", "chestnut", "hazelnut",
    "macadamia", "peanut", "pecan", "pine", "pistachio", "walnut", "barley", "buckwheat", "maize", "millet",
    "oats", "quinoa", "rice", "rye", "sorghum", "spelt", "wheat", "coffee", "tea", "cocoa"]

word = random.choice(word_list)
print(word)
space = ""

for letters in word:
    space += "_" 





n_space = list(space)
l_word = list(word)
n_of_lives = 6

f_space = ''.join(n_space) 



            



while n_of_lives is not 0:
    # f_space = ''.join(n_space)
    # print(f"Word to guess: {f_space}")
    print(f"Word to guess: {f_space}")
    
    a = input("Guess a letter: ").lower()
    
    if a in f_space:
        print(f"You've already guessed {a}")


    for l in l_word:
        if a == l:
            i = l_word.index(l)
            l_word[i] = '_'
            n_space[i] = a
            f_space = ''.join(n_space) 
    if a in word:
        print(f_space)
        print(lives[6-n_of_lives])
    else:
        n_of_lives -= 1
        print(f"You guessed {a}, that's not in the word. You lose a life.")
        print(lives[6-n_of_lives])
    if '_' not in f_space:
        print("You Won!")
        break
    
else:
    print(f'''***********************IT WAS {word}"! YOU LOSE**********************''')


