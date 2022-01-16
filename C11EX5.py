## C11 Files and Exception Handling
# Ex5 Write and read numbers
from random import randint


def main():
    # open the file for writing data
    outfile = open("numbers.txt", "w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close()

    # open file for reading data
    infile = open("numbers.txt", "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number, end=" ")
    infile.close()


main()
