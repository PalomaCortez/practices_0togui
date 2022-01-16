## C11 Files and Exception Handling
# Write Demo

def main():
    # open the file for output
    outfile = open("presidents.txt", "w")

    # write data to the file
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama\n")
    outfile.write("Donald Trump\n")

    outfile.close()

main()



