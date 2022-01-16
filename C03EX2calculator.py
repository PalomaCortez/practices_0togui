## Cap 3 - Mathematical functions, strings and objects
# C3EX2 Computes change

# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# convert the amount to cents
remaining_amount = int(amount * 100)

# Find the number of one dollars
number_of_one_dollars = remaining_amount // 100
remaining_amount = remaining_amount % 100

# Find the number of one quarters
number_of_one_quarters = remaining_amount // 25
remaining_amount = remaining_amount % 25

# Find the number of one dimes
number_of_one_dimes = remaining_amount // 10
remaining_amount = remaining_amount % 10

# Find the number of one nickels
number_of_one_nickels = remaining_amount // 5
remaining_amount = remaining_amount % 5

# Find the number of one pennies
number_of_one_pennies = remaining_amount

#Display the results
print("Your amount", amount, "consists of\n",
      "\t", number_of_one_dollars, "dollars \n",
      "\t", number_of_one_quarters, "quarters \n",
      "\t", number_of_one_dimes, "dimes \n",
      "\t", number_of_one_nickels, "nickels \n",
      "\t", number_of_one_pennies, "pennies ")


