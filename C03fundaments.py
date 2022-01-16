## Cap 3 - Mathematical functions, strings and objects

# math  - biblioteca de funções matemáticas
from math import *

x = 10.9
print("next integer is: ", ceil(x))
print("Previous integer is: ", floor(x))

x=5
print(pow(x,2))
print(x**2)

print(factorial(x))

print(log2(512))
print(log10(1000))
print(sqrt(9))

print(sin(radians(90)))

print(pi)

r = 2.5
area = pi * pow(r,2)
print(area)


#strings

x = 'Hello World'
print(x)

y = """This is a very long string
that stends for many lines
and can go eve
further
"""
print(y)
print(x[0])

str1 = x[1:7]
print(str1)
print(len(str1))

print(x.upper())
