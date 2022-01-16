## C12 Tuples, sets and dictionaries
# Set Demo

set1 = {"green", "red", "blue", "red"}  # create a set
print(set1)

set2 = set([7, 1, 2, 23, 2, 4, 5])  # create a set from a list
print(set2)

print("Is red in set1?", "red" in set1)
print("length is", len(set2))
print("max is", max(set2))
print("min is", min(set2))
print("sum is", sum(set2))

set3 = set1 | {"green", "yellow"}  # set union
print(set3)

set3 = set1 - {"green", "yellow"}
print(set3)

set3 = set1 & {"green", "yellow"}  # set intersection
print(set3)

set3 = set1 ^ {"green", "yellow"}  # set exclusive (^ and not ˆ)
print(set3)

list1 = list(set2)  # making a list from a set
print(set1 == {"green", "red", "blue"})

set1.add("yellow")
print(set1)

set1.remove("yellow")
print(set1)
