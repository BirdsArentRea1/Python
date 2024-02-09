import random
from winsound import Beep

#problem 1
def MultByFive(a, b, c, d, e):
    print(a, "+", b, "+", c, "-", d, "+", e, "is", a+b+c+d+e)
    
    
MultByFive(7,5,8,2,3)

print()

#problem 2
def ItemDropper():
    num = random.randrange(0,100)
    if num <20:
        print ("You got a Potion!")
    elif num <50:
         print ("You got a Cupcake!")
    elif num <75:
        print ("You got a Dirty Sock!")
    elif num <100:
        print ("You got Nothing! better luck next time")
    else:
        print("nothing spawned")
            
while True:
    ItemDropper()
    choice = input("Enter any key to continue....")
    
#problem 3
def beepboop():
    Beep(600, 500)
    Beep(550, 500)
    Beep(500, 500)
    Beep(450, 500)
    Beep(400, 500)
    
beepboop()
beepboop()
