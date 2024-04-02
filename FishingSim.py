import random

def fishing(): #start of function definition
    num = random.randrange(0, 100) #produces a number b/t 0-99
    if num < 10:
        print("you caught algae!")
        return "algae"
    if num < 20:
        print("you caught a trash!")
        return "trash"
    if num < 33:
        print("you caught a carp!")
        return "carp"
    if num < 66:
        print("you caught a woodskip!")
        return "woodskip"
    if num < 99:
        print("you caught a catfish!")
        return "catfish"
    
#function call---------------------------------------------
print(fishing(), "added to your inventory")
