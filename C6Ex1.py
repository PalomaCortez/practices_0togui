## Cap 6 - functions
#EX1 - Return Max

#Return the max of two numbers
def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result

def main():
    i = eval(input("Guive a value for number 1: "))
    j = eval(input("Guive a value for number 2: "))
    k = max(i,j) #call the max function
    print("The larger number of", i, "and", j, "is", k)

main() #call the main function



