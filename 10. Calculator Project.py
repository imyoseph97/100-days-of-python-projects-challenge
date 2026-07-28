art = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(art)



def calculator(a, b):
    if operation == "+":
        add = a + b
        return add
    elif operation == "-":
        sub = a - b
        return sub
    elif operation == "*":
        multi = a * b
        return multi
    elif operation == "/":
        div = a / b
        return div



not_finished = True

while not_finished:
    first = float(input("What's the first number?: "))

    operation = input("+ \n- \n* \n/ \nPick an operation: ")

    next = float(input("what's the next number?: "))    

    c = calculator(first, next)


    print(f"{first} + {next} = {c}")
    finish = input(f"Type 'y' to continue calculating with {c}, or type 'n' to start a new calculation: ")
    if finish == "y":
        while not_finished:
            another = float(input("What's the next nummber: "))
            
            
            
            print(f"{c} {operation} {another} = {calculator(c, another)}")
            finish = input(f"Type 'y' to continue calculating with {calculator(c, another)}, or type 'n' to start a new calculation: ")
            if finish == "y":
                c = eval(f"{c} {operation} {another}")
                not_finished = True
            else:
                break 