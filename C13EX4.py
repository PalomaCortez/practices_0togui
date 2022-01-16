## C13 Recursion
# EX4 - Recursive Selection Sort


def sort(lst):
    sort_helper(lst, 0, len(lst) - 1)  # sort the entire list


def sort_helper(lst, low, high):
    if low < high:
        # find the smallest element and its index in lst[low .. high]
        index_of_min = low
        mini = lst[low]
        for i in range(low + 1, high + 1):
            if lst[i] < mini:
                mini = lst[i]
                index_of_min = i

        # swap the smallest in lst[low .. high] with lst[low]
        lst[index_of_min] = lst[low]
        lst[low] = mini

        # sort the remaining list lst[low+1 .. high]
        sort_helper(lst, low + 1, high)


def main():
    lst = [3, 2, 1, 5, 9, 0]
    sort(lst)
    print(lst)


main()
