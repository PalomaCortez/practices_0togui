## C11 Files and Exception Handling
# Copy file Demo

import os.path
import sys

def main():
    # Prompt the user for entering the file names
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()

    # check if target file exists
    if os.path.isfile(f2):
        print(f2 + "already exists")
        sys.exit()

    # open the file for output
    infile = open(f1, "r")
    outfile = open(f2, "w")

    # copy from input file to output file
    count_lines = count_chars = 0
    for line in infile:
        count_lines += 1
        count_chars += len(line)
        outfile.write(line)
    print(count_lines, "lines and", count_chars, "chars copied.")

    infile.close()
    outfile.close()


main()
