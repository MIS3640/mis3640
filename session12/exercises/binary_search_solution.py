def binary_search(my_list, to_find):
    """
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list

    my_list: an ordered list of numbers from smallest to largest

    find: a number

    returns the index of x if x is in my_list, None if not.
    """
    left = 0
    right = len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if to_find == my_list[mid]:
            return mid
        elif to_find < my_list[mid]:
            right = mid - 1
        else:
            left = mid + 1


def main():
    test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
    test_list.sort()

    print(binary_search(test_list, -23))
    print(binary_search(test_list, 0))
    print(binary_search(test_list, 235425423))
    print(binary_search(test_list, 30))


if __name__ == "__main__":
    main()
