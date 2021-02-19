def sum_up(n):
    """sum up all the integers from 1 to N (inclusive)"""
    total = 0
    for i in range(n):
        # print(total, i)
        total += i
    return total


def main():
    result = sum_up(5)
    print(result)


if __name__ == "__main__":
    main()
