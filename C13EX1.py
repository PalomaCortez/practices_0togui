## C13 Recursion
# EX1 - Compute factorial

def main():
    n = eval(input("Enter a non-negative integer: "))
    print("Factorial of", n, "is", factorial(n))


def factorial(n):
    if n == 1:  # base case
        return 1
    else:
        return n * factorial(n-1)  # recursive call


main()
