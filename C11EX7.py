## C11 Files and Exception Handling
# Ex7 Text exception

def main():
    try:
        number1, number2 = eval(
            input("Enter two numbers, separated by a comma: "))
        result = number1 / number2
        print("Result is", result)
    except ZeroDivisionError:
        print("Division by zero!")
    except SyntaxError:
        print("A comma may be missing on the input.")
    except:
        print("Something wrong on the input.")
    else:
        print("No exceptions.")
    finally:
        print("The finally cause is executed.")


main()
