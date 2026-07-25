import random

l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
    '_', '`', '{', '|', '}', '~']
n = [0,1,2,3,4,5,6,7,8,9]

print("Welcome to PyPassword Generator!")

letters = int(input("How many letters would you like in your password? \n"))
symbols = int(input("How many symbols would like? \n"))
numbers = int(input("How many numbers woruld you like? \n"))

f1 = []


for i in range(letters):
    f1.append(random.choice(l))
for i in range(symbols):
    f1.append(random.choice(s))
for i in range(numbers):
    f1.append(random.choice(n))

    
print(f1)

random.shuffle(f1)
print(f1)

final = ""
for i in f1:
    final += str(i)


print(f"Your password is: {final}")
