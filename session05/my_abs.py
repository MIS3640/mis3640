# Exercise 3
def my_abs(number):
    """
    Print the absolute value of a number

    number: an integer or a floating point number
    """
    if number >= 0:
        print(number)
    else:
        print(-number)


my_abs(-10)

# Exercise 4
def my_abs(number):
    """
    Return the absolute value of a number

    number: an integer or a floating point number
    """
    if number >= 0:
        return number
    else:
        return -number


print(my_abs(-10))

# Exercise 5
def my_abs(number):
    """
    Return the absolute value of a number

    number: an integer or a floating point number
    """
    if isinstance(number, (int, float)):
        if number >= 0:
            return number
        else:
            return -number
    else:
        print('I don\'t know how to solve this')
        # raise TypeError


print(my_abs(-10))
