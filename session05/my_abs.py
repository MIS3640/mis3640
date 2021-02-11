def my_abs_5(number):
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


# print(my_abs_5(-10))
