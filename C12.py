## C12 Tuples, sets and dictionaries

# Tuples
my_tuple = ()
print(type(my_tuple))

this_tuple = ("apple", "orange")
print(this_tuple)

this_tuple = ("apple",)  # without the , it becomes a string
print(this_tuple)

this_tuple = 2, 'city', 19.4
print(this_tuple)
print(type(this_tuple))
x, y, z = this_tuple
print(x)
print(y)
print(z)

print(this_tuple[0])
print(this_tuple[1:])

# this_tuple[0] = 6
this_tuple = 2, 'city', [3, 45, 9]
this_tuple[2][1] = 10
print(this_tuple)

new_tuple = (1, 2, 2, 2, 3, 4)
print(new_tuple.count(2))
print(new_tuple.index(4))

print(5 in new_tuple)

# sets: unordered, mutable

A = {1, 2, 3, 3, 3, 4, 5, 6}  # the value 3 will only store once
print(A)
B = {}
print(type(B))
B = set()
print(type(B))
B.add(7)
print(B)
B.update([8, 9, 10])
print(B)

B.discard(7)  # does not matter if 7 is on the set or not
print(B)
B.remove(8)  # it gives an error if the value is not on the set
print(B)

A = {1, 2, 3, 4, 5, 6}
B = {2, 6, 7, 8, 9}
print(A.intersection(B))
print(A & B)
print(A.union(B))
print(A | B)
print(A.difference(B))
print(A - B)
print(B - A)
print(A.symmetric_difference(B))
print((A.union(B))-(A.intersection(B)))
# print(A ˆ B)

# Dictionaries

my_dict = {}
print(type(my_dict))
d1 = {1: 'cat', 2: 'dog', 'name': 'Jonh'}
print(d1)
print(d1['name'])

d2 = dict([(1, 'cat'), (2, 'dog')])
print(d2)
print(d2[2])
print(d2.get(2))

x = d2.pop(2)
print(x)
print(d2)

d2['phone'] = 1234565
print(d2)

new_dict = {'USA': 'Washington DC', 'France': 'Paris',
            'Egypt': 'Cairo', 'Germany': 'Berlin'}
print('USA' in new_dict)  # only search for keys
print(new_dict.keys())

print(new_dict.items())
for item in new_dict.items():
    print(item)

for i in new_dict:
    print(i)

for i in new_dict:
    print(new_dict[i])
