str_1 = "iPAD"
str_2 = "Babson"
str_3 = "python"


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


print("1")
print(any_lowercase1(str_1))
# True or False?
print(any_lowercase1(str_2))
# True or False?
print(any_lowercase1(str_3))
# True or False?


def any_lowercase2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"


print("2")
print(any_lowercase2(str_1))
# True or False?
print(any_lowercase2(str_2))
# True or False?
print(any_lowercase2(str_3))
# True or False?


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        # print(c, flag)
    return flag


print("3")
print(any_lowercase3(str_1))
# True or False?
print(any_lowercase3(str_2))
# True or False?
print(any_lowercase3(str_3))
# True or False?


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


print("4")
print(any_lowercase4(str_1))
# True or False?
print(any_lowercase4(str_2))
# True or False?
print(any_lowercase4(str_3))
# True or False?


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


print("5")
print(any_lowercase5(str_1))
# True or False?
print(any_lowercase5(str_2))
# True or False?
print(any_lowercase5(str_3))
# True or False?
