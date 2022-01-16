## Cap 9 - Lists
# EX 2 - Lotto numbers

# Create a list with 99 elements with the boolean False
is_covered = 99 * [False]
end_of_input = False
while not end_of_input:
    # read numbers from a string from the
    s = input("Enter a line of numbers separated by spaces: ")
    items = s.split()  # extract items from the string
    lst = [eval(x) for x in items]  # convert items to numbers

    for number in lst:
        if number == 0:
            end_of_input = True
        else:
            is_covered[number - 1] = True

    # Check whether all numbers (1 to 99) are covered
    all_covered = True  # assume all covered initially
    for i in range(99):
        if not is_covered[i]:
            all_covered = False  # find one number not covered
            break

    # display result
    if all_covered:
        print("The tickets cover all numbers")
    else:
        print("The tickets don`t cover all numbers")
