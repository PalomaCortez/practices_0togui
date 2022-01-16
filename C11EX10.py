## C11 Files and Exception Handling
# Ex10 Process exception object


try:
    number = eval(input("Enter a number: "))
    print("The number entered is: ", number)

except NameError as ex:
    print("Exception:", ex)
