def gcd_recur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    # Your code here
    print("Current a, b:", a, b)  # for testing
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)


if __name__ == "__main__":
    # print(gcd_recur(2, 12))
    # print(gcd_recur(6, 12))
    print(gcd_recur(9, 12))
    # print(gcd_recur(17, 12))
