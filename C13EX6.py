## C13 Recursion
# EX6 - Directory Size
import os


def main():
    # prompt the user to enter a directory or a file
    path = input("Enter a directory or a file: ").strip()

    # Display the size
    try:
        print(get_size(path), "bytes")
    except:
        print("Directory or file does not exist")


def get_size(path):
    size = 0  # Store the total size of all files

    if not os.path.isfile(path):
        lst = os.listdir(path)  # All the files and directories
        for subdirectory in lst:
            size += get_size(path + "/" + subdirectory)  # "\\" for windows
    else:  # Base case, it is a file
        size += os.path.getsize(path)  # accumulate file size

    return size


main()
