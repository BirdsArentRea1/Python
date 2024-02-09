def simple_calculator(num1, num2, operation):
    if operation == "add":
        return num1+num2
    else:
        return num1-num2
    
print(simple_calculator(10, 2, "subtract"))
print(simple_calculator(10, 2, "add"))

print()

def Candy(num):
    while num > 0:
        print("You can have", num, "pieces of candy")
        choice = input("Do you want (S)nickers or (M)&Ms?")
        if choice == 'S':
            print("here's a Snickers")
        elif choice == 'M':
            print("here's a M&Ms")
        num-=1
        
Candy(5)

print()

def OobaAdder():
   word = input("please enter a word.")
   print(word+"ooba")
   
OobaAdder()
