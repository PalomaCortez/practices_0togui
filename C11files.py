## C11 Files and Exception Handling

# fin = open('files/LWP.txt', 'r')

# first_line = fin.readline()
# print(first_line)
# second_line = fin.readline()
# print(second_line)
# thirt_line = fin.readline()
# print(thirt_line)

# print(fin.readlines())

# for line in fin:
#     print(line)

# print(fin.read(10))

# fin = open('files/LWP.txt', 'a')
#
# fin.write("\nThis is a new line that we hae just written.\n")
# new_lines = ["This is line1\n",
#              "Thisis line2\n",
#              "This is line3\n"]
# fin.writelines(new_lines)

fin = open('files/new_file.txt', 'w')
# new_lines = ["This is line1\n",
#              "This is line2\n",
#              "This is line3\n"]
# fin.writelines(new_lines)
#
# new_lines = ["This overwrites the 1st line\n",
#              "This overwrites the 2nd line\n",
#              "This overwrites the 3rd line\n"]
# fin.writelines(new_lines)

#fin.close()

try:
    fin = open('files/LWPw.txt', 'r')

    first_line = fin.readline()
    print(first_line)
    second_line = fin.readline()
    print(second_line)
    thirt_line = fin.readline()
    print(thirt_line)
    fin.close()

except:
    print("Error: we can not find or open your file. Please check yous code")



