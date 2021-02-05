def f(a, b):
    """Return sum of A and B, product of A and B"""
    # print(a)
    # result = a + b
    # return result
    return a + b, a * b


# Scope

# x = 3
# y = 4
# c = f(x, y)
# print(c)
# print(result)
# print(a)


def f2():
    """Print Hi"""
    print('Hi')
    return None


# print(f2())
# a = f2() # f2() is called/executed, assign the returned value to a
# print(a)

# f2()

def my_abs(x):
    """Retun the absolute value of X"""
    # Pseudo-code
    # 1. Check the type of x
    # 2. based type of x, do different things
    # 2.1  if x is an int or float
    #          if x is negative, return the opposite of x (-x)
    #          otherwise, just return x
    # 2.2  if x is not int or float
    #       do something else



def square(a):
    """Calculate square of A"""
    result = a ** 2
    return result


b = square(10)
print(b)
