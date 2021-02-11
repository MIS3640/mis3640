def factorial(n):
    """Return the factorial of N"""
    result = 1
    if n == 1:
        return result
    result = n * factorial(n - 1)
    print("current n =", n)
    print("current result =", result)
    return result


if __name__ == "__main__":
    # print(factorial(1))
    # print(factorial(3))
    print(factorial(10))
