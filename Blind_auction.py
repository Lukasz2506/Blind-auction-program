#The blind auction program
#100 Days of code, Angela Yu
#You can take part in a blind auction and bid it!

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os
print(logo)

def Max_bid(attendents_dictionary):
    value_list = []
    for key in auction_attendents:
        value_list.append(auction_attendents[key])
    max_value = max(value_list)
    return max_value

def winner(attendents, max_value):
    for key in auction_attendents:
        if auction_attendents[key] == max_value:
            max_bidder = key   
    return max_bidder

next_person = "yes"
auction_attendents = {}


while  next_person == "yes":
    
    person = input("What is your name?").strip().capitalize()
    value = round(float(input("What is your bid? $")),2)
    print(value)
    auction_attendents[person] = value   
    next_person = input("Would like to add next person (yes, no)?").strip().lower()
    os.system('cls')
  
highest_bid = Max_bid(auction_attendents)
Winner = winner(auction_attendents, highest_bid)
print(f"{Winner} Wins the auction with a bid ${highest_bid}!!! Congratulations!!!")
