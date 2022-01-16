## Cap 6 - functions
#EX3 - test GCD function

from C6EX2 import gcd

# Prompt the user to get two integers
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest common divisor for", n1, "and", n2, "is", gcd(n1, n2))
