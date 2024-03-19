#1) Write a function named "calculate_health" that takes three parameters: current health, damage received, and armor. When called, it calculates
#and returns the new health value by multiplying the damage received by the armor, and then subtracting that value from the current health. 
#Test the function by calling it with the following numbers: 100, 10, and .5 (the answer should be 95). Store the return value of the function in a variable, 
#and then print the variable. 

def calculate_health(health, damage, armor):

    health = health - damage*armor

    return health

print(calculate_health(100,10,0.5))

#2) Write a function named "average_of_five" that takes five integer parameters. When called, it calculates the average by adding all
#of the numbers together and dividing the result by five. 
#Test the function by calling it inside a print function with the following numbers: 10, 20, 30, 40, 50 (the answer should be 30). 

def avarage_five(num1,num2,num3,num4,num5):

    sum = num1+num2+num3+num4+num5
    return sum/5
print(avarage_five(10,20,30,40,50))
