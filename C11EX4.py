## C11 Files and Exception Handling
# Ex4 Append file Demo

def main():
    # open the file for appendind data
    outfile = open("info.txt", "a")
    outfile.write("\nPython is interpreted\n")
    outfile.close()


main()
