## Cap 5 - Loops
#EX3 - Multiplication table

print("          Multiplication table")
# Display the number title
print("    |", end = '')
for j in range(1, 10):
    print(" ", j, end = '')
print() #jump to new line
print("----------------------------------------")

#Display the table body
for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        #display the product and align properly
        print(format(i * j, "2d"), end = '')
    print() #jump to new line

