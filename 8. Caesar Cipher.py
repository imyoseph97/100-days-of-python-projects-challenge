import string


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

letters = list(string.ascii_lowercase)


def cc(inputs, shift):
    encrypted = ""
    decrypted = ""

    if ed == 'encode':
        for l in inputs:
            position = letters.index(l)
            index = position + shift
            if index < 26:
                encrypted += letters[index]
            else:
                encrypted += letters[index - 26]
        print(f"Here's the encoded result: {encrypted}")

    elif ed == 'decode':
        for l in inputs:
            position = letters.index(l)
            index = position - shift
            if index >= 0:
                decrypted += letters[index]
            else:
                decrypted += letters[index + 26]
        print(f"Here's the decoded result: {decrypted}")
    else:
        print("please enter either 'encode' or 'decode'.")

try_again = True

while try_again:

    ed = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    
    cc(input("Type your message: \n").lower(), int(input("Type the shift number: \n")))

    again = input("Type 'yes' if you want to do it again. Otherwise type 'no'. ").lower()
    
    if again == 'yes':
        try_again = True
    else:
        try_again = False



    
