logo = r"""              ___________
                         \        /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
                  
                  
                  """

print(logo)
other_bidders = True

bidders = {}
max = 0

while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is bid?: "))
    bidder = input("Are there any other bidedrs? Type 'yes' or 'no'.").lower()
    bidders[name] = bid
    if bidder == "yes":
        other_bidders = True
    elif bidder == "no":
        other_bidders = False
        for b in bidders:
            if bidders[b] > max:
                max =  bidders[b]
    for key, value in bidders.items():
        if value == max:
            print(f"the winner is {key} with a bid of ${max}")
            break
        

    
    


