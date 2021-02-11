def fib(n):
    """Return the Nth Fibonacci number."""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(5))
    print(fib(2))
