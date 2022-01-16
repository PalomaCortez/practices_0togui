## Cap 9 - Lists
# some practices with lists

a = []
print("a has a ", type(a))

my_list = [1, 2, 3, 4, 5]

print("my_list[0] = ", my_list[0])
print("my_list[4] = ", my_list[4])
print("len(my_list) = ", len(my_list))

print("my_list[1:3] = ", my_list[1:3])
print("my_list[:3] = ", my_list[:3])
print(my_list[1:])

new_list = ['dog', 2, 10.5, True, 'a']
print(new_list)
print(new_list[0])

new_list[1] = 'cat'
print(new_list)

new_list.append(5)  # add to the end of the list. Takes only one argument
print(new_list)

# to add a new iten in between the itens of the list you need more arguments
new_list.insert(2, 'elephant')
print(new_list)

# for i in (new_list):
#     if i == 'cat':
#         print("cat found")

if 'cat' in new_list:
    print("cat in in new_list")

if 'lion' in new_list:
    print("lion in in new_list")

for x in new_list:
    print(x)

new_list.remove('cat')  # remove by value
print(new_list)

new_list.pop(1)  # remove by index
print(new_list)

new_list.pop()  # remove the last item
print(new_list)

list1 = new_list  # in that case the list 1 referes to the location of new_list. It is not a coppy
print(list1)
# new_list.pop()
# print(list1)

# to make an actual copy
list1 = new_list.copy()
new_list.pop()
print("list1: ", list1)
print("new_list: ", new_list)


odd_num_range = range(1, 10, 2)
print(odd_num_range)
num = list(odd_num_range)
print(num)

# sum_of_num = 0
# for j in num:
#     sum_of_num += j
# print(sum_of_num)

print(sum(num))
print(max(num))
print(min(num))
print(sum(num)/len(num))

# Multidimensional lists
mlist = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]  # two dimensional list

# threed_list = [[[], []], [] ]
print(mlist)
print(mlist[0])
print(mlist[0][1])
print(mlist[2][2])
print(mlist[0:2])
mlist.append([13, 14,15])
print(mlist)

for x in mlist:
    for y in x:
        print(y)
