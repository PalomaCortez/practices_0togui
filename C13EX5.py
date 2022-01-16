## C13 Recursion
# EX5 - Recursive Binary Search


def recursive_bin_sch(lst, key):
    low = 0
    high = len(lst) - 1
    return recurs_bin_helper(lst, key, low, high)


def recurs_bin_helper(lst, key, low, high):
    if low > high:  # the list has being exhausted without a match
        return - low - 1

    mid = (low + high) // 2
    if key < lst[mid]:
        return recurs_bin_helper(lst, key, low, mid - 1)
    elif key == lst[mid]:
        return mid
    else:
        return recurs_bin_helper(lst, key, mid + 1, high)


def main():
    lst = [3, 5, 6, 8, 9, 12, 34, 36]
    print(recursive_bin_sch(lst, 3))
    print(recursive_bin_sch(lst, 4))


main()
