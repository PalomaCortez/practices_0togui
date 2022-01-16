## C13 Recursion

# ex: Factorial of a number
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!

# iterative algorithm (approach)
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact
#
# print(factorial(5))

# RECURSIVE algorithm (approach)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
