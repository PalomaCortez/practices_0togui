## C13 Recursion
# EX2 - Compute Fibonacci

def main():
    index = eval(input("Enter a index for a Fibonacci number: "))
    # Find and display the Fibonacci number
    print("The Fibonacci number at index", index, "is", fib(index))


def fib(index):
    if index == 0:  # base case
        return 0
    elif index == 1:
        return 1
    else:  # Reduction and recursive calls
        return fib(index - 1) + fib(index - 2)


main()
