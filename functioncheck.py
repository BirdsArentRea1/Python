def frog_jump(num):
    for i in range(num):
        print("jump #", i, "Ribbit")
        
frog_jump(11)

print()

def guessnum(target):
    num = -1
    while target != num:
        num = int(input("guess a number 1-100"))
        if num == target:
            print("you guessed right!")
        elif num > target:
            print("too high!")
        else:
            print("too low!")
            
guessnum(42)
            
print()

def vampire(age, garlic):
    if age > 1000 and garlic == False:
        print("your a vampire!")
    else:
        print("not a vampire")
vampire(1000, True)

print()

def launch(fuel, astro):
    if astro*100<fuel:
        print("Launch Successful!")
        return "Launch Successful!"
    else:
        print("insufficient fuel")
        return "Insufficient fuel"
print(launch(500,3))
