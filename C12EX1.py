## C12 Tuples, sets and dictionaries
# Tuple Demo

tuple1 = ("green", "red", "blue")  # Create a tuple
print(tuple1)

tuple2 = tuple([7, 1, 2, 23, 4, 5])  # create a tuple from a list
print(tuple2)

print("length is", len(tuple2))  # use function len
print("max is", max(tuple2))  # use max
print("min is", min(tuple2))  # use min
print("sum is", sum(tuple2))

print("The first element is", tuple2[0])

tuple3 = tuple1 + tuple2  # combine two tuples
print(tuple3)

tuple3 = 2 * tuple1
print(tuple3)

print(tuple2[2:4])
print(tuple1[-1])

print(2 in tuple2)

for v in tuple1:
    print(v, end=' ')
print()

list1 = list(tuple2)
list1.sort()
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print(tuple4)
print(tuple4 == tuple5)
