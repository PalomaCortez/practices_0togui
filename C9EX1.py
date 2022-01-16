## Cap 9 - Lists
# EX 1 - Data Analysis

NUMBER_OF_ELEMENTS = 5  # for simplicity we will use 5 instead of 100
numbers = []
sum_it = 0

for i in range(NUMBER_OF_ELEMENTS):
    value = eval(input("Enter a new number: "))
    numbers.append(value)
    sum_it += value

average = sum_it/NUMBER_OF_ELEMENTS

count = 0  # Thw number of elements above average
for i in range(NUMBER_OF_ELEMENTS):
    if numbers[i] > average:
        count += 1

print("the average is", average)
print("The number of elements above the average is", count)
