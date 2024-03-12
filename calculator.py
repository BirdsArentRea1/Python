operand_one = 0.0
operand_two = 0.0



sum = 0.0
diff = 0.0
quotient = 0.0
product = 0.0 
remainder = 0.0


print("Input the first operand.")
operand_one = float(input())
print("FIRST>", operand_one)

print("Input the second operand.")
operand_two = float(input())
print("SECOND>", operand_two)


sum = operand_one + operand_two 
diff = operand_one - operand_two
quotient = operand_one // operand_two
product = operand_one * operand_two
remainder = operand_one % operand_two

operand_one = operand_one + operand_two
operand_onediff = operand_one - operand_two

sum = round(sum, 1)
diff = round(diff, 1)
quotient = round(quotient, 1)
product = round(product, 1)


print("The sum of", operand_one, "and", operand_two, "is", sum )
print("The difference of", operand_one, "and", operand_two, "is", diff )
print("The quotient of", operand_one, "and", operand_two, "is", quotient )
print("The product of", operand_one, "and", operand_two, "is", product)
print("The remainder of", operand_one, "and", operand_two, "is", remainder )
