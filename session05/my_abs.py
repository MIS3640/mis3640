def my_abs_5(number):
    """Return the absolute value of a number"""
    if isinstance(number, (int, float)):
        if number >= 0:
            return number
        else:
            return -number
    else:
        print('I don\'t know how to solve this')


def f():
    print('Hi')


def main():
    print(my_abs_5(-10))
    f()


if __name__ == "__main__":
    main()
