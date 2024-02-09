import random

def questions(num):
    for i in range(num):
        print("question", i + 1)
        
questions(100)

print()

def banana(scoop, banana):
    if banana*3>scoop:
        print("heres a banana split")
    else:
        print("heres a plain sunday")
            
banana(0,0)

print()

def namegen():
    num = random.randrange(0,75)
    if num < 25:
        return "a"
    elif num <50:
        return "b"
    elif num <75:
        return "c"
    
print(namegen())
